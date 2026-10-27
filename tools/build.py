#!/usr/bin/env python3
"""Sestaví statickou HTML verzi návrhu z .dc.html souborů.

Použití:  python3 tools/build.py   (spouštět z kořene repa)
Vstup:    redesign/src/*.dc.html, redesign/src/canvas.json
Výstup:   redesign/<Nazev>.html  (samostatné stránky, otevřitelné i přes file://)
"""
import json, re, html, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'redesign' / 'src'
OUT = ROOT / 'redesign'
IMG_DIR = OUT / 'img'

BUILT = {}
canvas = json.loads((SRC / 'canvas.json').read_text(encoding='utf-8'))
imgs = {p.stem: p.name for p in IMG_DIR.iterdir()} if IMG_DIR.exists() else {}


def parse(name):
    s = (SRC / f'{name}.dc.html').read_text(encoding='utf-8')
    title = re.search(r'<title>(.*?)</title>', s, re.S)
    lang = re.search(r'<html[^>]*lang="([^"]+)"', s)
    body = re.search(r'<x-dc>(.*)</x-dc>', s, re.S).group(1)
    helmet = ''
    m = re.search(r'<helmet>(.*?)</helmet>', body, re.S)
    if m:
        helmet = m.group(1)
        body = body[:m.start()] + body[m.end():]
    logic = re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>', s, re.S)
    props = re.search(r"data-props='([^']*)'", s)
    return {
        'title': html.unescape(title.group(1).strip()) if title else name,
        'lang': lang.group(1) if lang else 'cs',
        'body': body, 'helmet': helmet,
        'logic': logic.group(1) if logic else '',
        'props': json.loads(html.unescape(props.group(1))) if props else {},
    }


def fix_refs(text, depth_prefix=''):
    def blob(m):
        bid = m.group(1)
        if bid not in imgs:
            print(f'  ! chybí obrázek {bid}', file=sys.stderr)
            return m.group(0)
        return f'img/{imgs[bid]}'
    text = re.sub(r'/_blob/([0-9a-f]{32})', blob, text)
    text = re.sub(r'href="(?:\./)?([A-Za-z0-9_-]+)\.dc\.html', r'href="\1.html', text)
    # homepage = kořen webu
    text = text.replace('href="Main.html', 'href="../index.html')
    return text


def deps(name, seen=None):
    seen = seen if seen is not None else []
    if name in seen:
        return seen
    seen.append(name)
    for child in re.findall(r'<dc-import[^>]*\bname="([^"]+)"', parse(name)['body']):
        deps(child, seen)
    return seen


def script_safe(text):
    if re.search(r'</script', text, re.I):
        raise SystemExit('šablona obsahuje </script> – nelze bezpečně vložit')
    return text


def build(name):
    main = parse(name)
    board = canvas['boards'].get(f'{name}.dc.html', {})
    title = board.get('title') or main['title']
    helmets, seen_h = [], set()
    blocks = []
    for d in deps(name):
        p = parse(d)
        hm = p['helmet'].strip()
        if hm and hm not in seen_h:
            seen_h.add(hm)
            helmets.append(f'<!-- styly: {d} -->\n{hm}')
        blocks.append(f'<script type="text/x-dc-template" data-dc="{d}">{script_safe(fix_refs(p["body"]))}</script>')
        if p['logic'].strip():
            blocks.append(f'<script type="text/x-dc-logic" data-dc="{d}">{script_safe(p["logic"])}</script>')
    # samostatný fragment (popup, menu): vycentrovat v náhledové šířce
    pw = (main['props'].get('$preview') or {}).get('width')
    frame = ''
    if not board.get('expand') and pw:
        frame = (f'<style>html{{background:#E5E7EB}}#dc-root{{max-width:{pw}px;margin:32px auto;'
                 'background:#fff}}</style>')
    out = f'''<!doctype html>
<html lang="{main['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · DSK Stavebniny</title>
{fix_refs(chr(10).join(helmets))}
{frame}
</head>
<body data-dc-root="{name}">
<div id="dc-root"></div>
{chr(10).join(blocks)}
<script src="vendor/react.production.min.js"></script>
<script src="vendor/react-dom.production.min.js"></script>
<script src="js/dc-runtime.js"></script>
</body>
</html>
'''
    (OUT / f'{name}.html').write_text(out, encoding='utf-8')
    BUILT[name] = out
    return title


def md(text):
    """Minimální Markdown → HTML (nadpisy, odstavce, tabulky, seznamy, `kód`, **tučně**)."""
    def inline(s):
        s = html.escape(s, quote=False)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        return s
    out, lines, i = [], text.strip().splitlines(), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1; continue
        if ln.startswith('```'):
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            out.append('<pre><code>' + html.escape('\n'.join(lines[i + 1:j])) + '</code></pre>')
            i = j + 1; continue
        m = re.match(r'(#{1,4})\s+(.*)', ln)
        if m:
            lv = len(m.group(1)) + 1
            out.append(f'<h{lv}>{inline(m.group(2))}</h{lv}>'); i += 1; continue
        if ln.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            t = '<table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in rows[0]) + '</tr></thead><tbody>'
            t += ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in rows[1:])
            out.append(t + '</tbody></table>'); continue
        if re.match(r'\s*[-*]\s', ln):
            items = []
            while i < len(lines) and re.match(r'\s*[-*]\s', lines[i]):
                items.append(re.sub(r'^\s*[-*]\s', '', lines[i])); i += 1
            out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>'); continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r'(#{1,4}\s|\||```|\s*[-*]\s)', lines[i]):
            para.append(lines[i]); i += 1
        out.append('<p>' + inline(' '.join(para)) + '</p>')
    return '\n'.join(out)


DOC_CSS = '''
@font-face{font-family:"Exo 2";src:url(FONTS/Exo2-Variable.ttf) format("truetype");font-weight:100 900;font-style:normal}
@font-face{font-family:"Exo 2";src:url(FONTS/Exo2-Italic-Variable.ttf) format("truetype");font-weight:100 900;font-style:italic}
*{box-sizing:border-box}
body{margin:0;background:#F4F5F7;color:#1A1E23;font:400 16px/24px "Exo 2","Segoe UI",system-ui,sans-serif}
header.top{background:#009FE3;color:#002433}
header.top .in,main{max-width:1200px;margin:0 auto;padding:24px 16px}
header.top h1{margin:0;font:700 32px/38px "Exo 2",sans-serif}
header.top p{margin:4px 0 0}
header.top nav{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:12px}
header.top nav a{color:#002433;font-weight:700}
h2{font:700 26px/32px "Exo 2",sans-serif;color:#005980;margin:40px 0 12px}
h3{font:700 19px/24px "Exo 2",sans-serif;color:#005980;margin:0 0 4px}
h4,h5{color:#003D57;margin:20px 0 8px}
a{color:#007DB2}
code{background:#E5E7EB;border-radius:4px;padding:1px 5px;font-size:.9em}
pre{background:#1A1E23;color:#F4F5F7;border-radius:6px;padding:12px;overflow:auto}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:14px;line-height:20px;background:#fff}
th,td{border:1px solid #E5E7EB;padding:6px 10px;text-align:left;vertical-align:top}
th{background:#EBF9FF}
.card{background:#fff;border:1px solid #E5E7EB;border-radius:6px;margin:16px 0;overflow:hidden}
.card .meta{padding:16px 20px;border-bottom:1px solid #E5E7EB}
.card .meta p{margin:6px 0 0;font-size:14px;line-height:20px;color:#5B646E}
.card .stage{overflow:auto}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(260px,100%),1fr));gap:16px}
.tile{display:block;background:#fff;border:1px solid #E5E7EB;border-radius:6px;padding:16px 20px;text-decoration:none;color:#1A1E23}
.tile:hover{border-color:#007DB2}
.tile strong{display:block;color:#005980;font-size:18px}
.tile span{font-size:14px;color:#5B646E}
.doc{background:#fff;border:1px solid #E5E7EB;border-radius:6px;padding:8px 24px 16px;margin:16px 0}
.sw{display:flex;flex-wrap:wrap;gap:8px}
.sw div{width:120px;font-size:12px;line-height:16px}
.sw i{display:block;height:48px;border-radius:4px;border:1px solid #E5E7EB;margin-bottom:4px}
'''


def build_ds():
    ds = ROOT / 'design-system'
    comps = sorted(p for p in (ds / 'components').iterdir() if p.is_dir())
    groups = {}
    for c in comps:
        prev = c / 'preview.html'
        if not prev.exists():
            continue
        src = prev.read_text(encoding='utf-8')
        m = re.search(r'<!--\s*@dsCard(.*?)-->', src)
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1))) if m else {}
        readme = (c / 'README.md').read_text(encoding='utf-8') if (c / 'README.md').exists() else ''
        readme = re.sub(r'^#\s+.*\n', '', readme.strip())
        groups.setdefault(attrs.get('group', 'Obálka'), []).append((c.name, attrs.get('subtitle', ''), md(readme), src))
    # barvy z tokens.json
    tok = json.loads((ds / 'tokens.json').read_text(encoding='utf-8'))
    swatches = [(t['name'], t['value']) for t in tok.get('color', {}).get('tokens', [])
                if isinstance(t.get('value'), str) and t['value'].startswith('#')]
    sw_html = '<div class="sw">' + ''.join(
        f'<div><i style="background:{v}"></i><code>{html.escape(n)}</code><br>{v}</div>' for n, v in swatches) + '</div>'
    docs = [('README.md', 'Přehled'), ('breakpoints.md', 'Breakpointy'), ('spacing.md', 'Rozestupy'),
            ('naming.md', 'Pojmenování'), ('struktura.md', 'Struktura e-shopu'), ('audit.md', 'Audit komponent'),
            ('api/tokens.md', 'Tokeny')]
    nav = ''.join(f'<a href="#{html.escape(g)}">{html.escape(g)}</a>' for g in groups) + \
        '<a href="#barvy">Barvy</a><a href="#dokumentace">Dokumentace</a><a href="assets/">Assety</a><a href="../prehled.html">← Přehled stránek</a>'
    body = [f'<header class="top"><div class="in"><h1>DSK Stavebniny — design systém</h1>'
            f'<p>Tokeny, komponenty a pravidla pro redesign e-shopu dskstavebniny.cz.</p><nav>{nav}</nav></div></header><main>']
    for g, items in groups.items():
        body.append(f'<h2 id="{html.escape(g)}">{html.escape(g)}</h2>')
        for name, sub, rd, src in items:
            body.append(f'<section class="card" id="c-{name}"><div class="meta"><h3>{name}</h3>'
                        f'<p>{html.escape(sub)}</p>{rd}</div><div class="stage">{src}</div></section>')
    body.append(f'<h2 id="barvy">Barvy</h2><div class="doc">{sw_html}</div>')
    body.append('<h2 id="dokumentace">Dokumentace</h2>')
    for f, t in docs:
        p = ds / f
        if p.exists():
            text = p.read_text(encoding='utf-8')
            text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
            text = text.split('\n---\n\n## Consuming this system')[0]
            body.append(f'<details class="doc"><summary><h3 style="display:inline">{t}</h3> <code>{f}</code></summary>{md(text)}</details>')
    body.append('</main>')
    page = f'''<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Design systém · DSK Stavebniny</title>
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="components/bundle.css">
<style>{DOC_CSS.replace('FONTS', 'fonts')}</style>
</head>
<body>
{chr(10).join(body)}
</body>
</html>
'''
    (ds / 'index.html').write_text(page, encoding='utf-8')
    # přehled assetů
    rows = []
    for p in sorted((ds / 'assets').rglob('*')):
        if p.is_file() and p.name != 'index.html':
            rel = p.relative_to(ds / 'assets').as_posix()
            rows.append(f'<a class="tile" href="{html.escape(rel)}"><img src="{html.escape(rel)}" alt="" '
                        f'style="max-width:100%;max-height:180px;display:block;margin-bottom:8px;background:#003D57">'
                        f'<span>{html.escape(rel)}</span></a>')
    (ds / 'assets' / 'index.html').write_text(f'''<!doctype html><html lang="cs"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Assety · DSK Stavebniny</title>
<style>{DOC_CSS.replace('FONTS', '../fonts')}</style></head><body>
<header class="top"><div class="in"><h1>Assety design systému</h1><nav><a href="../index.html">← Design systém</a></nav></div></header>
<main><div class="grid">{''.join(rows)}</div></main></body></html>
''', encoding='utf-8')
    print('  ✓ design-system/index.html')


def build_index(built):
    pages = [b for b in built if b[2].get('expand')]
    parts = [b for b in built if not b[2].get('expand')]
    tile = lambda n, t: f'<a class="tile" href="redesign/{n}.html"><strong>{html.escape(t)}</strong><span>redesign/{n}.html</span></a>'
    page = f'''<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DSK Stavebniny — redesign e-shopu</title>
<style>{DOC_CSS.replace('FONTS', 'design-system/fonts')}</style>
</head>
<body>
<header class="top"><div class="in"><h1>DSK Stavebniny — redesign e-shopu</h1>
<p>Statická HTML verze návrhu a design systému.</p></div></header>
<main>
<h2>Stránky</h2>
<div class="grid">{''.join(tile(n, t) for n, t, _ in pages)}</div>
<h2>Plovoucí vrstvy a mobilní menu</h2>
<div class="grid">{''.join(tile(n, t) for n, t, _ in parts)}</div>
<h2>Design systém</h2>
<div class="grid"><a class="tile" href="design-system/index.html"><strong>Komponenty, tokeny a pravidla</strong><span>design-system/index.html</span></a>
<a class="tile" href="design-system/assets/index.html"><strong>Assety</strong><span>logo, ikony, referenční snímky z Figmy</span></a></div>
</main>
</body>
</html>
'''
    (ROOT / 'prehled.html').write_text(page, encoding='utf-8')
    print('  ✓ prehled.html')


def main():
    order = canvas.get('order') or sorted(p.name for p in SRC.glob('*.dc.html'))
    built = []
    for f in order:
        n = f.replace('.dc.html', '')
        built.append((n, build(n), canvas['boards'].get(f, {})))
        print('  ✓', n)
    build_ds()
    build_index(built)
    build_home()
    build_404()


def build_home():
    """Kořenový index.html = homepage (Main), cesty míří do redesign/ přes <base>."""
    s = BUILT['Main']
    s = s.replace('<head>', '<head>\n<base href="redesign/">', 1)
    (ROOT / 'index.html').write_text(s, encoding='utf-8')
    print('  ✓ index.html (homepage)')


def build_404():
    """Kořenový 404.html pro GitHub Pages. Base se dopočítá podle adresy,
    protože 404 se servíruje na libovolné cestě (i na projektové stránce /repo/)."""
    if 'Chyba404' not in BUILT:
        return
    s = BUILT['Chyba404']
    js = ("<script>(function(){var p=location.pathname.split('/').filter(Boolean);"
          "var b=(/github\\.io$/.test(location.hostname)&&p.length)?'/'+p[0]+'/redesign/':'/redesign/';"
          "document.write('<base href=\"'+b+'\">');})();</script>")
    s = s.replace('<head>', '<head>\n' + js, 1)
    (ROOT / '404.html').write_text(s, encoding='utf-8')
    print('  ✓ 404.html (stránka nenalezena)')


if __name__ == '__main__':
    main()
