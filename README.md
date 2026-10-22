# DSK Stavebniny – redesign e-shopu (klikací prototyp)

Samostatný web pro otestování návrhu na desktopu, tabletu a mobilu. Funguje na GitHub Pages i po otevření `index.html` přímo z disku.

## Stránky

| Stránka | Soubor |
|---|---|
| Homepage | `index.html` |
| Sortiment (rozcestník e-shopu) | `sortiment.html` |
| Výpis kategorie (Fasády, maltové směsi) | `kategorie.html` |
| Detail produktu (Styramik THS-04G) | `detail.html` |

Stránky jsou mezi sebou prolinkované: logo → homepage, Sortiment / Celý sortiment → rozcestník, kategorie → výpis, produkty → detail, drobečková navigace zpět.

## Co jde vyzkoušet

Hero slider, megamenu (hover/klik), Články (rozbalovací menu), mobilní menu, našeptávač vyhledávání (klik do pole), mini košík (hover na košík), karusely se šipkami, filtr ve výpisu, strom kategorií, výběr prodejny, záložky a lightbox fotky v detailu, popup „Vložili jste do košíku“ (tlačítko Koupit v detailu), skrývací hlavička při scrollu.

## Zveřejnění na GitHub Pages

1. Nahrajte obsah této složky do kořene repozitáře (včetně složky `assets/` a souboru `.nojekyll`).
2. **Settings → Pages → Build and deployment → Deploy from a branch**, větev `main`, složka `/ (root)`.
3. Web poběží na `https://<uživatel>.github.io/<repozitář>/`.

## Poznámky

- `assets/dc-runtime.js` skládá stránky a obsluhuje interakce; komponenty (megamenu, popupy…) jsou vložené přímo ve stránkách.
- Písmo Exo 2 se načítá z Google Fonts (bez internetu se použije náhradní písmo).
- Ceny, skladovosti a texty jsou ilustrační. Odkazy na dosud nenavržené stránky (košík, účet, články…) zatím nikam nevedou.
