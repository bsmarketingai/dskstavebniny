# DSK Stavebniny – redesign e-shopu (klikací náhled)

Statický HTML export návrhu pro testování na desktopu, tabletu a mobilu.

## Stránky

| Stránka | Soubor |
|---|---|
| Homepage | `Main.dc.html` (výchozí, `index.html` na ni přesměruje) |
| Sortiment (rozcestník) | `Sortiment.dc.html` |
| Výpis kategorie | `Kategorie.dc.html` |
| Detail produktu | `Detail.dc.html` |

Popupy, megamenu, mobilní menu, filtr, našeptávač a výběr prodejny jsou součástí stránek (soubory `MegaMenu`, `MobilMenu`, `Filtr`, `KosikPopup`, `KosikMini`, `ProdejnaModal`, `Naseptavac`) a načítají se automaticky.

## Zveřejnění na GitHub Pages

1. Nahrajte celý obsah této složky do kořene repozitáře (včetně `support.js`, složky `assets/` a souboru `.nojekyll`).
2. V repozitáři: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, větev `main`, složka `/ (root)`.
3. Za minutu bude náhled na `https://<uživatel>.github.io/<repozitář>/`.

Stránky je nutné otevírat přes web server (GitHub Pages, nebo lokálně např. `python3 -m http.server`) — při otevření souboru přímo z disku (`file://`) se nenačtou vložené komponenty.

## Poznámky

- `support.js` je runtime, který skládá stránky a obsluhuje interakce (karusely, megamenu, popupy, záložky).
- Písmo Exo 2 se načítá z Google Fonts.
- Data, ceny a skladovosti jsou ilustrační.
