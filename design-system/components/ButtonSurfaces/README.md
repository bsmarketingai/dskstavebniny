# ButtonSurfaces

Která tlačítka smí stát na kterém podkladu — přesně podle stránek. Na každém podkladu je vždy jedna hlavní akce a k ní vedlejší.

| Podklad | Hlavní akce | Vedlejší akce | Příklady |
|---|---|---|---|
| **Bílá** (obsah) | `--conversion` / `--primary` | `--soft`, `--tool`, `--ghost`, `--outline`, `--secondary` | výpis, detail, košík, formuláře |
| **Světlá** `primary-50` (FAQ, nákupní box detailu, Pomoc s řezáním, rychlé výběry) | `--conversion` | `--soft`, `--tool` | Koupit + číselník + porovnání v detailu |
| **Šedá** `secondary-100` (popup, 404) | `--conversion` | `--neutral` | Přejít k objednávce + Pokračovat v nákupu |
| **Hlavní lišta** `primary-500` | `--conversion` (AI asistent), košík `--primary` s cenou | Hledat `--primary --joined`, ikony Porovnat / Přihlásit (bílé, 48 px) | hlavička |
| **Kategoriová lišta** `primary-600` | Sortiment (`primary-300`, text `primary-900`, 40 px) | bílé odkazy 56 px | hlavička |
| **Tmavá** `primary-800` / `primary-900` (hero, bannery, newsletter, lišta košíku, patička) | `--on-dark` nebo `--conversion` | `--on-dark-outline`, `--secondary` (Na začátek stránky) | hero, Sezóna zateplování, kalkulačka, newsletter, lišta košíku |
| **NZU zelená** `nzu-green` | bílé tlačítko s textem `primary-800` / `nzu-green` | `--on-dark-outline` | jen stránka Nová zelená úsporám |

Zakázané kombinace: konverzní a modré tlačítko vedle sebe ve stejné velikosti jako dvě hlavní akce; `--soft` nebo `--tool` na tmavé ploše; bílý text přímo na `primary-500`.
