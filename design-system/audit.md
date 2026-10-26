# Audit komponent

Audit návrhu e-shopu (homepage, výpis kategorie, detail, megamenu, mobilní menu, mini košík, popup košíku, výběr prodejny, filtr, patička) — co se opakuje a jestli to má komponentu. Stav k 22. 10. 2026.

## Hotové komponenty

Všechny mají třídy v `components/bundle.css` (prefix `dsk-`, jen tokeny, žádné pevné hodnoty) a kartu s ukázkou.

| Opakuje se | Kde | Komponenta |
| --- | --- | --- |
| tlačítka 7 rolí, 3 velikosti | všude | Button |
| štítky, počítadla, stav prodejny | karty, hlavička, patička, modal | Badge |
| vyhledávání, pole, výběr, checkbox, čip | hlavička, filtr, newsletter, detail | FormControls |
| číselník + Do košíku | karta, detail | QuantityStepper |
| cena s/bez DPH, sleva, skladovost | karta, detail, mini košík, popup | PriceStock |
| karta produktu | HP karusely, výpis, související, alternativní | ProductCard |
| dlaždice podkategorie, karta sortimentu | HP, výpis, megamenu | CategoryTile |
| nadpis sekce + šipky | HP, detail | SectionHeading |
| drobečky, záložky, stránkování | výpis, detail | Navigation |
| akordeon | detail, filtr, patička, mobilní menu | Accordion |
| nejbližší prodejna, doprava zdarma | patička, modal, popup | InfoBars |
| kontakt, prodejna, doprava, platby | patička | FooterTiles |
| výhoda | pás Proč nakupovat | Usp |
| modal, popover, šuplík | popupy, filtr, prodejny | Dialog |
| ikony v hlavičce | hlavička | HeaderActions |

## Sjednoceno během auditu

- Počítadla měla tři různé styly → jeden `dsk-counter` (oranžový).
- Ikona košíku byla dvojí → všude Tabler `truck-loading`.
- Ikony dopravy se lišily mezi patičkou, hero a pásem výhod → všude `car-crane` a garáž.
- Ikona mínus jako čára s nulovou výškou se nevykreslovala → obdélník.
- Mřížky s pevným minimem (300 / 280 px) přetékaly na 320 px → `minmax(min(…,100%),1fr)`.
- Hlavička na XXS–XS: logo 36 px, Hledat jen jako ikona, otevírací doba skrytá, Kontakty jako ikona v horní liště, akční ikony 40 px pod 420 px.

## Chybí — připravit

| Co | Proč | Priorita |
| --- | --- | --- |
| ProductCard layout B (1000–1149 px) a A (≥1150 px, tabulka) | požadavek Master Design Systemu | vysoká |
| Košík a objednávka — 3 kroky (košík, kontaktní údaje, kontrola) + ukazatel kroků | hlavní konverzní cesta | vysoká |
| Výběr dopravy a platby (radio karty s cenou) | krok 1 košíku | vysoká |
| Prázdný košík | stav existuje na webu | střední |
| Stránka vyhledávání (Nalezené stránky + produkty) | /hledat/ | střední |
| Přihlášení / registrace (rozbalovací mini formulář v hlavičce) | hlavička | střední |
| Rychlý náhled produktu (lupa na kartě) | ikona už je v kartě | střední |
| Stavy formulářů: chyba, úspěch, povinné pole | newsletter, objednávka | střední |
| Toast „Přidáno do porovnání / oblíbených“ | akce v detailu | nízká |
| Skeleton načítání karet a výpisu | Načíst dalších 24 | nízká |
| Termalica a Auto-moto | čeká na rozhodnutí o stromu kategorií | — |
