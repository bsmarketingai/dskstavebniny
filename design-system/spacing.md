# Rozestupy

Základní jednotka je **4 px**. Mezi 0 a 16 px jdeme po 4 (plus mikro krok 2 px), nad 16 px se kroky zvětšují: 20, 24, 32, 40, 48, 64, 80. Hodnoty mimo škálu (6, 10, 14, 18 px…) nepoužíváme — když se nevejde, sáhni po sousedním kroku, ne po mezihodnotě.

| Token | Hodnota | Kde |
|---|---|---|
| `space-0-5` | 2 px | štítky, fokus |
| `space-1` | 4 px | ikona–text ve štítku |
| `space-2` | 8 px | ikona–text v tlačítku, skupiny |
| `space-3` | 12 px | malé prvky, dlaždice |
| `space-4` | 16 px | karty, pole, tlačítka |
| `space-5` | 20 px | panely na mobilu |
| `space-6` | 24 px | gutter desktop, panely |
| `space-8` | 32 px | okraj stránky desktop |
| `space-10` | 40 px | pásy na mobilu |
| `space-12` | 48 px | sekce na mobilu |
| `space-16` | 64 px | sekce na desktopu |
| `space-20` | 80 px | rezerva |

## Pravidlo blízkosti

Čím víc spolu věci souvisí, tím menší mezera: uvnitř prvku 4–8, mezi prvky jedné skupiny 8–12, mezi skupinami v kartě 12–16, mezi kartami gutter, mezi sekcemi `section-gap`. Nadpis sekce je od svého obsahu vždy blíž (24) než od předchozí sekce (48/64).

## Responzivní rozestupy

Pět rozestupů se mění s breakpointem; v CSS jsou to proměnné na `:root`.

| | XXS | XS | S | M | L | XL | XXL |
|---|---|---|---|---|---|---|---|
| `--page-margin` | 12 | 16 | 24 | 32 | 32 | 32 | 32 (obsah max 1560) |
| `--gutter` | 12 | 16 | 16 | 24 | 24 | 24 | 24 |
| `--section-gap` | 48 | 48 | 48 | 64 | 64 | 64 | 64 |
| `--band-pad` | 40 | 40 | 40 | 48 | 48 | 48 | 48 |
| `--card-pad` | 12 | 12 | 16 | 16 | 16 | 16 | 16 |

```css
:root { --page-margin: 12px; --gutter: 12px; --section-gap: 48px; --band-pad: 40px; --card-pad: 12px; }
@media (min-width: 420px) { :root { --page-margin: 16px; --gutter: 16px; } }
@media (min-width: 550px) { :root { --page-margin: 24px; --card-pad: 16px; } }
@media (min-width: 820px) { :root { --page-margin: 32px; --gutter: 24px; --section-gap: 64px; --band-pad: 48px; } }
```

## Výšky ovládacích prvků

`control-sm` 32 px jen pro čipy, `control-md` 44 px je výchozí (minimální dotyková plocha), `control-lg` 52 px pro hlavní akci v panelu. Vnitřní vodorovný padding tlačítek je `space-4` (16), u ikonových tlačítek se šířka rovná výšce.
