# ProductCard

Karta produktu ve výpisu i karuselech (`article.pcard` na stránkách) — layout **C (stacked)**. Pořadí: obrázek se štítky (pod sebou vlevo nahoře) → název (700 15/20, max. 3 řádky) → krátký popis (`secondary-600`) → skladovost `dsk-stk` → cena s DPH s jednotkou „/ ks“, přeškrtnutá cena vpravo, cena bez DPH → číselník + čtvercové Do košíku. Rámeček `secondary-200`, `radius-md`, padding těla 16. Stejná karta je ve všech karuselech (homepage, detail, košík) — nevymýšlet jiné.

**Hover:** karta se zvedne o 6 px s měkkým stínem (300 ms) a název se podtrhne. Karusel má nahoře 8 px rezervu, aby se zvednutá karta neořízla. Bez hoveru karty stín nemají. Obsah karty nebalit do dalšího `<article>` (globální hover).

Layouty B (1000–1149 px) a A (≥ 1150 px, tabulka) z Master Design Systemu nejsou navržené — výpis používá C i na desktopu (4 sloupce vedle stromu kategorií).
