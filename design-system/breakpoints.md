# Breakpointy

Sedm pojmenovaných breakpointů XXS–XXL, mobile-first (`min-width`). Návrh začíná na 320 px; XXS platí i pro užší displeje.

| Název | Rozsah | Sloupce | Gutter | Okraj | Produktů v řadě | Sidebar |
| --- | --- | --- | --- | --- | --- | --- |
| XXS | 0–419 px (návrh od 320) | 4 | 12 px | 12 px | 1 | ne |
| XS | 420–549 px | 4 | 16 px | 16 px | 2 | ne |
| S | 550–819 px | 8 | 16 px | 24 px | 2 | ne |
| M | 820–999 px | 8 | 24 px | 32 px | 3 | ne |
| L | 1000–1149 px | 12 | 24 px | 32 px | 3 | ano, 280 px |
| XL | 1150–1439 px | 12 | 24 px | 32 px | 4 | ano, 280 px |
| XXL | ≥ 1440 px | 12 | 24 px | 32 px, obsah max 1560 px | 5 | ano, 280 px |

**Maximální šíře webu je 1560 px obsahu.** Od 1624 px (1560 + 2 × 32) obsah dál neroste, jen se zvětšují okraje a plné pozadí pásů (hlavička, newsletter, patička) pokračuje do stran. Figma rámce 1885–1936 px jsou XXL.

## Chování hlavičky

- XXS–S (pod 820 px): utility lišta (prodejna, Otevřeno, ikona kontaktů), hlavní lišta s logem, ikonami Porovnat / Přihlásit / Košík (40 px, pod 420 px 36 px, bez mezer) a tmavým hamburgerem 44 px; pod ní vyhledávání s lupou a AI asistent jako ikona. Kategorie a Služby / Články v mobilním menu (vlastní scroll, výška max. `100dvh − 172px`). Klepnutí na košík otevře popup mini košíku.
- M: vyhledávání se vejde do hlavní lišty, kategorie stále v menu.
- L–XXL: tři pásy — utility, hlavní lišta s popisky ikon a cenou v košíku, kategoriová lišta s tlačítkem Sortiment (megamenu), Služby ▾, Články ▾ a dalšími odkazy.

## Další prahy použité na stránkách

- **820 px** — šipky karuselů pod produkty, H2 22/28, kroky košíku zkrácené, lišta košíku ve dvou řádcích, tabulky jako karty.
- **640 px** — dlaždice materiálů (Řezání oceli) jako řádky, našeptávač s kategoriemi pod produkty.
- **1150 px** — tabulka košíku plná (pod tím koš vpravo v kartě položky).

## CSS

```css
/* XXS je výchozí stav */
@media (min-width: 420px)  { /* XS  */ }
@media (min-width: 550px)  { /* S   */ }
@media (min-width: 820px)  { /* M   */ }
@media (min-width: 1000px) { /* L   */ }
@media (min-width: 1150px) { /* XL  */ }
@media (min-width: 1440px) { /* XXL */ }

.container { max-width: calc(1560px + 2 * var(--page-margin)); margin: 0 auto; padding-inline: var(--page-margin); }
```

```scss
$breakpoints: (xxs: 0, xs: 420px, s: 550px, m: 820px, l: 1000px, xl: 1150px, xxl: 1440px);
$content-max: 1560px;
```

## Model platformy BSSHOP: buckety, ne kaskáda

Rozsahy odpovídají platformě BSSHOP (ověřeno na bigboy.cz): platforma dělí CSS do samostatných souborů podle media query a načítá jen ten pro aktuální šířku. Buckety se nepřekrývají ani nemají mezery; krajní mají jen jednu podmínku.

| Bucket | Media query |
| --- | --- |
| XXS | `(max-width: 419px)` |
| XS | `(min-width: 420px) and (max-width: 549px)` |
| S | `(min-width: 550px) and (max-width: 819px)` |
| M | `(min-width: 820px) and (max-width: 999px)` |
| L | `(min-width: 1000px) and (max-width: 1149px)` |
| XL | `(min-width: 1150px) and (max-width: 1439px)` |
| XXL | `(min-width: 1440px)` |

Plus základní bundle bez media query, který platí vždy. Mobile-first `min-width` ukázky výše dávají stejný výsledek; pro produkci ve BSSHOP piš styly do bucketů.

## Layouty produktové karty

| Layout | Rozsah | Buckety |
| --- | --- | --- |
| C — stacked card | < 1000 px | XXS–M |
| B — compact block | 1000–1149 px | L |
| A — full table | ≥ 1150 px | XL–XXL |

Prahy 1000 a 1150 px kopírují systémovou škálu platformy, nejsou odvozené ze součtu šířek sloupců.
