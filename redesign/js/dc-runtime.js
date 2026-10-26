/*
 * dc-runtime.js — malý samostatný runtime pro statický export návrhů (.dc.html).
 * Vykreslí šablony <x-dc> ({{díry}}, <sc-if>, <sc-for>, <dc-import>, style-hover)
 * pomocí Reactu 18 (vendor/). Logika komponent = třída `Component extends DCLogic`.
 */
(function () {
  'use strict';
  var R = window.React, RD = window.ReactDOM, h = R.createElement;

  // ---------- registry šablon a tříd ----------
  var TPL = {}, CLS = {}, SRC = {};
  document.querySelectorAll('script[type="text/x-dc-template"]').forEach(function (s) {
    var t = document.createElement('template');
    t.innerHTML = s.textContent;
    TPL[s.dataset.dc] = t.content;
  });
  document.querySelectorAll('script[type="text/x-dc-logic"]').forEach(function (s) {
    SRC[s.dataset.dc] = s.textContent;
  });

  // ---------- hover styly ----------
  var hoverSheet = document.createElement('style'), hoverSeen = {};
  document.head.appendChild(hoverSheet);
  function hoverClass(css) {
    var hsh = 0;
    for (var i = 0; i < css.length; i++) hsh = (hsh * 31 + css.charCodeAt(i)) | 0;
    var cls = 'dch' + (hsh >>> 0).toString(36);
    if (!hoverSeen[cls]) {
      hoverSeen[cls] = 1;
      var decl = css.split(';').map(function (d) { d = d.trim(); return d ? d.replace(/\s*!important\s*$/, '') + ' !important' : ''; }).filter(Boolean).join(';');
      hoverSheet.appendChild(document.createTextNode('.' + cls + ':hover{' + decl + '}\n'));
    }
    return cls;
  }

  // ---------- díry {{ }} ----------
  var HOLE = /\{\{\s*([^}]+?)\s*\}\}/g, WHOLE = /^\s*\{\{\s*([^}]+?)\s*\}\}\s*$/;
  function lookup(path, scope) {
    if (path === 'true') return true;
    if (path === 'false') return false;
    if (path === 'null') return null;
    if (/^-?\d+(\.\d+)?$/.test(path)) return Number(path);
    if (/^(['"]).*\1$/.test(path)) return path.slice(1, -1);
    var parts = path.split('.'), v = scope;
    for (var i = 0; i < parts.length; i++) { if (v == null) return undefined; v = v[parts[i]]; }
    return v;
  }
  function interp(str, scope) {
    return str.replace(HOLE, function (_, p) { var v = lookup(p, scope); return v == null ? '' : String(v); });
  }
  function value(str, scope) {
    var m = WHOLE.exec(str);
    return m ? lookup(m[1], scope) : (str.indexOf('{{') >= 0 ? interp(str, scope) : str);
  }

  // ---------- atributy ----------
  var EVENTS = {};
  ['Click','DoubleClick','KeyDown','KeyUp','KeyPress','MouseEnter','MouseLeave','MouseOver','MouseOut','MouseDown','MouseUp',
   'Scroll','Change','Input','Focus','Blur','Submit','PointerDown','PointerUp','PointerEnter','PointerLeave','TouchStart','TouchEnd','Wheel','ContextMenu']
    .forEach(function (e) { EVENTS['on' + e.toLowerCase()] = 'on' + e; });
  var ATTR = { 'class': 'className', 'for': 'htmlFor', tabindex: 'tabIndex', readonly: 'readOnly', maxlength: 'maxLength',
    minlength: 'minLength', colspan: 'colSpan', rowspan: 'rowSpan', autocomplete: 'autoComplete', autofocus: 'autoFocus',
    inputmode: 'inputMode', enterkeyhint: 'enterKeyHint', contenteditable: 'contentEditable', crossorigin: 'crossOrigin',
    srcset: 'srcSet', frameborder: 'frameBorder', allowfullscreen: 'allowFullScreen', spellcheck: 'spellCheck',
    referrerpolicy: 'referrerPolicy', datetime: 'dateTime', novalidate: 'noValidate', accesskey: 'accessKey', 'xlink:href': 'xlinkHref',
    'xmlns:xlink': 'xmlnsXlink' };
  var BOOL = { checked: 1, disabled: 1, open: 1, hidden: 1, required: 1, selected: 1, multiple: 1, readonly: 1, autofocus: 1, novalidate: 1, allowfullscreen: 1 };
  var VOID = { area: 1, base: 1, br: 1, col: 1, embed: 1, hr: 1, img: 1, input: 1, link: 1, meta: 1, source: 1, track: 1, wbr: 1 };
  var TABLEISH = { table: 1, thead: 1, tbody: 1, tfoot: 1, tr: 1, colgroup: 1 };

  function camel(s) { return s.replace(/-([a-z])/g, function (_, c) { return c.toUpperCase(); }); }
  function styleObj(str) {
    var o = {};
    // rozdělit podle ; mimo závorky (url(...), rgba(...))
    var depth = 0, cur = '', parts = [];
    for (var i = 0; i < str.length; i++) {
      var c = str[i];
      if (c === '(') depth++; else if (c === ')') depth--;
      if (c === ';' && depth === 0) { parts.push(cur); cur = ''; } else cur += c;
    }
    parts.push(cur);
    parts.forEach(function (d) {
      var k = d.indexOf(':'); if (k < 0) return;
      var name = d.slice(0, k).trim(), val = d.slice(k + 1).trim();
      if (!name) return;
      o[name.indexOf('--') === 0 ? name : camel(name.replace(/^-ms-/, 'ms-'))] = val;
    });
    return o;
  }

  function buildProps(el, scope, isSvg, key) {
    var p = { key: key }, hovers = [], cls = [];
    var tag = el.localName;
    for (var i = 0; i < el.attributes.length; i++) {
      var a = el.attributes[i], n = a.name, raw = a.value;
      if (n.indexOf('hint-') === 0) continue;
      if (EVENTS[n]) { var fn = value(raw, scope); if (typeof fn === 'function') p[EVENTS[n]] = fn; continue; }
      if (n === 'ref') { var r = value(raw, scope); if (r) p.ref = r; continue; }
      if (n === 'style-hover') { var hv = interp(raw, scope); if (hv.trim()) hovers.push(hoverClass(hv)); continue; }
      if (n === 'style') { p.style = styleObj(interp(raw, scope)); continue; }
      if (n === 'class') { var cv = value(raw, scope); if (cv) cls.push(String(cv)); continue; }
      var v = value(raw, scope);
      if (BOOL[n]) {
        var b = (raw === '' || raw === n) ? true : !(v === false || v === 'false' || v == null);
        if (n === 'checked' && tag === 'input') p.defaultChecked = b;
        else if (n === 'selected') { if (b) p.__selected = true; }
        else p[ATTR[n] || n] = b;
        continue;
      }
      if (n === 'value' && (tag === 'input' || tag === 'textarea' || tag === 'select')) { p.defaultValue = v; continue; }
      if (ATTR[n]) { p[ATTR[n]] = v; continue; }
      if (n.indexOf('aria-') === 0 || n.indexOf('data-') === 0) { p[n] = v; continue; }
      if (isSvg && n.indexOf('-') > 0) { p[camel(n)] = v; continue; }
      p[n] = v;
    }
    cls = cls.concat(hovers);
    if (cls.length) p.className = cls.join(' ');
    return p;
  }

  // ---------- vykreslení šablony ----------
  function renderNodes(list, scope, isSvg, parentTag) {
    var out = [];
    for (var i = 0; i < list.length; i++) {
      var r = renderNode(list[i], scope, isSvg, i, parentTag);
      if (r === null || r === undefined) continue;
      out.push(r);
    }
    return out;
  }

  function renderNode(node, scope, isSvg, key, parentTag) {
    if (node.nodeType === 3) {
      var t = node.nodeValue;
      if (!t.trim() && (TABLEISH[parentTag] || /\n/.test(t) && parentTag === 'select')) return null;
      return t.indexOf('{{') >= 0 ? interp(t, scope) : t;
    }
    if (node.nodeType !== 1) return null;
    var tag = node.localName;
    if (tag === 'helmet') return null;
    if (tag === 'sc-if') {
      var c = value(node.getAttribute('value') || '', scope);
      return c ? h(R.Fragment, { key: key }, renderNodes(node.childNodes, scope, isSvg, parentTag)) : null;
    }
    if (tag === 'sc-for') {
      var arr = value(node.getAttribute('list') || '', scope) || [], as = node.getAttribute('as') || 'item';
      if (!Array.isArray(arr)) arr = Array.from(arr);
      return h(R.Fragment, { key: key }, arr.map(function (it, idx) {
        var s = Object.create(scope); s[as] = it; s.$index = idx;
        return h(R.Fragment, { key: idx }, renderNodes(node.childNodes, s, isSvg, parentTag));
      }));
    }
    if (tag === 'dc-import') {
      var name = node.getAttribute('name'), props = { key: key };
      for (var i = 0; i < node.attributes.length; i++) {
        var a = node.attributes[i];
        if (a.name === 'name' || a.name.indexOf('hint-') === 0) continue;
        props[camel(a.name)] = value(a.value, scope);
      }
      return h(getComponent(name), props);
    }
    var svg = isSvg || tag === 'svg';
    var realTag = svg ? node.tagName.replace(/^svg:/, '') : tag;
    if (svg && realTag === realTag.toUpperCase()) realTag = realTag.toLowerCase();
    var p = buildProps(node, scope, svg, key);
    if (tag === 'select') {
      var sel = node.querySelector('option[selected]');
      if (sel && p.defaultValue === undefined) p.defaultValue = sel.getAttribute('value') || sel.textContent;
    }
    delete p.__selected;
    if (VOID[tag]) return h(realTag, p);
    var src = tag === 'template' ? node.content.childNodes : node.childNodes;
    var kids = renderNodes(src, scope, svg && tag !== 'foreignobject', tag);
    if (tag === 'textarea') { p.defaultValue = kids.join(''); return h(realTag, p); }
    return h.apply(null, [realTag, p].concat(kids.length ? [kids] : []));
  }

  // ---------- DCLogic ----------
  function DCLogic(props) { R.Component.call(this, props); this.state = this.state || {}; }
  DCLogic.prototype = Object.create(R.Component.prototype);
  DCLogic.prototype.constructor = DCLogic;
  DCLogic.prototype.renderVals = function () { return {}; };
  DCLogic.prototype.render = function () {
    var vals = this.renderVals() || {};
    var scope = Object.assign({}, this.props, vals);
    return h(R.Fragment, null, renderNodes(this.__tpl.childNodes, scope, false, 'div'));
  };
  window.DCLogic = DCLogic;

  function getComponent(name) {
    if (CLS[name]) return CLS[name];
    var tpl = TPL[name];
    if (!tpl) { CLS[name] = function () { return h('div', { style: { padding: 16, color: '#C8102E' } }, 'Chybí komponenta ' + name); }; return CLS[name]; }
    var Base;
    if (SRC[name]) {
      // zdroj je třída `class Component extends DCLogic { … }` (ES2015 class) – vyhodnotíme ji se závislostmi v rozsahu
      Base = new Function('DCLogic', 'React', SRC[name] + '\n;return Component;')(DCLogic, R);
    } else {
      Base = function Component(p) { DCLogic.call(this, p); };
      Base.prototype = Object.create(DCLogic.prototype);
    }
    var C = class extends Base {};
    C.prototype.__tpl = tpl;
    C.displayName = name;
    CLS[name] = C;
    return C;
  }

  // ---------- start ----------
  var rootName = document.body.dataset.dcRoot;
  var mount = document.getElementById('dc-root');
  RD.createRoot(mount).render(h(getComponent(rootName), {}));
})();
