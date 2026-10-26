# DSK Stavebniny — redesign e-shopu

Statická HTML verze návrhu redesignu e-shopu dskstavebniny.cz a jeho design systému.
Exportováno z Claude artifactů „DSK Stavebniny — redesign e-shopu“ (Design) a „DSK Stavebniny“ (Design System), 23. 10. 2026.

`index.html` v kořeni je rovnou homepage e-shopu, takže na GitHub Pages se web otevře jako funkční web a dá se proklikat na sortiment, výpis kategorie i detail produktu. Přehled všech stránek, vrstev a design systému je v `prehled.html`. Vše funguje bez serveru (stačí otevřít v prohlížeči) i na GitHub Pages.

## Struktura

```
index.html                 homepage (kopie redesign/Main.html s <base href="redesign/">)
prehled.html               přehled stránek, vrstev a design systému
redesign/
  Main.html …              stránky a vrstvy návrhu (vygenerované, interaktivní)
  src/*.dc.html            zdrojové artboardy (originální formát z Claude Design)
  src/canvas.json          rozložení plátna, názvy artboardů, pořadí
  src/ds/dsk/tokens.json   kopie tokenů design systému použitá v návrhu
  img/                     fotky a obrázky použité v návrhu
  js/dc-runtime.js         malý runtime, který vykresluje .dc šablony (React 18)
  vendor/                  React 18.3.1 (MIT)
design-system/
  index.html               galerie komponent, barvy, dokumentace
  tokens.css / tokens.json design tokeny
  components/bundle.css    CSS komponent (prefix dsk-)
  components/*/            README a ukázka každé komponenty
  *.md                     breakpointy, rozestupy, pojmenování (BSSHOP), struktura, audit
  fonts/                   Exo 2 (variabilní)
  assets/                  logo, ikony, referenční snímky z Figmy
tools/build.py             znovu vygeneruje HTML ze zdrojů
```

## Stránky

| Soubor | Obsah |
| --- | --- |
| `redesign/Main.html` | Homepage |
| `redesign/Sortiment.html` | Sortiment (rozcestník e-shopu) |
| `redesign/Kategorie.html` | Výpis kategorie |
| `redesign/Detail.html` | Detail produktu |
| `redesign/MegaMenu.html`, `MobilMenu.html` | Megamenu, mobilní menu |
| `redesign/KosikPopup.html`, `KosikMini.html` | Popup Vložili jste do košíku, mini košík |
| `redesign/Filtr.html`, `ProdejnaModal.html`, `Naseptavac.html` | Šuplík filtru, výběr prodejny, našeptávač |

Stránky jsou interaktivní (megamenu, mobilní menu, výběr prodejny, karusely, záložky v detailu, filtr).

## Úpravy

Zdrojem pravdy jsou `redesign/src/*.dc.html`. Po úpravě spusť:

```sh
python3 tools/build.py
```

Skript přegeneruje `redesign/*.html`, `design-system/index.html` `prehled.html` a `index.html` (homepage). Odkazy `X.dc.html` se přepíšou na `X.html`, obrázky `/_blob/<id>` na `img/<id>.<přípona>`.
