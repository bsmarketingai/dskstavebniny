# Stock

Skladovost — **jedna komponenta všude**, kde je produkt: karta ve výpisu a karuselu, detail, mini košík, popup Vložili jste do košíku, našeptávač, tabulka košíku. Na stránkách prototypu třídy `.stk / .stk-my / .stk-my--no / .stk-all`.

## Skladba `dsk-stk`

Dva řádky pod sebou (mezera 1 px):

1. **Vybraná prodejna** `dsk-stk__my` — název prodejny z horní lišty (výchozí Jesničánky) + počet. 600 13/18, ikona 16 px.
   - **Skladem** (počet > 0): zelený check, `success`, počet tučně: „Jesničánky: **48 ks**“.
   - **Není na prodejně** (0 ks): hodiny, `main-700`, počet netučně: „Jesničánky: 0 ks“ — zboží jde převézt z jiné prodejny.
2. **Součet** `dsk-stk__all` — „Celkem na 9 prodejnách: **5 258 ks**“, 500 12/17 `secondary-600`, odsazený 22 px (zarovnaný s textem nad ním, ne s ikonou). Počet se nezalamuje.

Velikost `--lg` (14/20 a 13/18) jen v nákupním boxu detailu. V úzkém sloupci (tabulka košíku) se smí zalomit text „Celkem na 9 prodejnách:“, nikdy počet.

## Přehled po prodejnách `dsk-avail`

Jen v detailu produktu pod nákupním boxem: rozbalovací panel (bílý, rámeček `secondary-200`, `radius-md`, padding 0 20). Hlavička: špendlík + „Skladem na prodejnách: 4 z 9“ (700 16/22 `primary-700`), chevron. Řádky všech 9 prodejen: název vlevo, počet vpravo, oddělené hairline; prodejny se zbožím tučně `success`, ostatní `secondary-600`. Pod seznamem poznámka „Stav skladu aktualizujeme každých 60 minut.“ (13/18).

## Pravidla

- Žádné jiné zápisy skladovosti („Skladem 5 258 ks“, „Na objednávku“, štítky) nepoužívat.
- Počet ve `dsk-stk__my` musí odpovídat řádku vybrané prodejny v `dsk-avail`.
- Barva nikdy sama nenese význam — vždy s ikonou (check / hodiny).
