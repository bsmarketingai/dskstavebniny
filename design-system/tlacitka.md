# Tlačítka

Úplný soupis tlačítek použitých na stránkách redesignu (změřeno na vykreslených stránkách 27. 10. 2026, desktop 1440 px a mobil 390 px). Každé tlačítko = `dsk-btn` + role + velikost (karta Button). Sloupec **Na stránce** uvádí, kde se rozměr či rádius ještě liší od definice — ty položky jsou ke sjednocení (viz Audit).

## Konverzní — `dsk-btn--conversion` (`main-500`, text `primary-900`)

| Tlačítko | Velikost | Podklad | Stránky | Na stránce |
|---|---|---|---|---|
| Do košíku (ikona) v kartě produktu | `--icon` 44 | bílá karta | výpis, karusely, vyhledávání, porovnání, košík, blog | rádius 4 px |
| AI asistent | `--field` 48 | hlavní lišta `primary-500` | hlavička (mobil jen ikona 48) | — |
| Spočítat spotřebu | `--field` 48 | banner kalkulačky `primary-900` | výpis kategorie | — |
| Chci výpočet | `--field` 48 | homepage banner | homepage | — |
| Poslat poptávku | `--field` 48 | bílá | homepage, služby | — |
| Přihlásit (newsletter) | `--field` 48 | box newsletteru `primary-800` | všechny stránky s newsletterem | rádius 4 px |
| Koupit | `--lg` 52, písmo 18 | nákupní box `primary-50` | detail | — |
| Přejít k objednávce | `--lg` 52 | bílá / popup | popup Vložili jste, mini košík | — |
| Přihlásit se | `--lg` 52, celá šířka | modal | přihlášení | — |
| Zpět na úvod | `--lg` 52 | bílá | 404 | — |
| Odeslat poptávku | `--lg` 52 | karta formuláře | poptávka | rádius 4 px |
| Pokračovat / Odeslat objednávku | `--xl` 64 dvouřádkové (mobil 48) | lišta košíku `primary-800` | košík krok 1–3 | — |

## Tmavé — `dsk-btn--primary` (`primary-800`, bílý text)

| Tlačítko | Velikost | Podklad | Stránky | Na stránce |
|---|---|---|---|---|
| Hledat | `--field` 48 `--joined` (mobil ikona 48) | hlavní lišta | hlavička | — |
| Košík s cenou | 48, ikona + cena + počítadlo | hlavní lišta | hlavička (mobil ikona 36–40 bez podkladu) | — |
| Hamburger | `--icon` 44 | hlavní lišta | mobil | — |
| Filtrovat | 44 | bílá | výpis, vyhledávání | rádius 4 px |
| Vybrat svoji prodejnu | 44 | bílá | kontakty | rádius 4 px |
| Nastavit jako svoji prodejnu | 44 | karta prodejny | modal prodejen | — |
| Ověření dodavatelé, Více informací, Kontakty a prodejny | 44 / 48 | bílá | homepage, blog | — |
| Vybraná záložka | 44 | bílá | detail | — |
| Šipka Další v karuselu | `--icon` 44 (mobil 52) | bílá | homepage, detail, košík, blog | rádius 4 px |
| Aktuální stránka | 44 | bílá | výpis, vyhledávání, blog | rádius 4 px |

## Modré — `dsk-btn--secondary` (`primary-600`, bílý text)

| Tlačítko | Velikost | Stránky | Na stránce |
|---|---|---|---|
| Další (stránkování) | 44 | výpis, vyhledávání, blog | rádius 4 px |
| Zobrazit 36 produktů | `--lg` 52 | šuplík filtru | rádius 4 px |
| Na začátek stránky | `--lg` 52, písmo 17 | patička (všechny stránky) | — |
| Rychlá poptávka | `--lg` 52 | Řezání oceli | — |

## Jemné — `dsk-btn--soft` (bílé, 1 px `primary-200`, text `primary-700`)

| Tlačítko | Velikost | Stránky | Na stránce |
|---|---|---|---|
| Máte účet? Přihlaste se | 44 | košík krok 2 | — |
| Registrujte se | 44 | modal přihlášení | výška 46 |
| Kde řežeme, Kontakty na provozovny | `--lg` 52 | Řezání oceli | — |
| Zjistit více | `--field` 48 | NZU (karty programů) | průhledné pozadí |
| Rychlá poptávka | `--field` 48 | blog | rámeček `secondary-400`, text `primary-800` |

## Ostatní role

| Role | Tlačítko | Velikost | Stránky | Na stránce |
|---|---|---|---|---|
| `--outline` | Načíst dalších 24 / 12 | `--field` 48 | výpis, vyhledávání, blog | rádius 4 px |
| `--tool` | Předchozí v karuselu | `--icon` 44 (mobil 52); neaktivní `secondary-100` + ikona `secondary-400` | homepage, detail, košík | rádius 4 px |
| `--tool` | Čísla stránek, Předchozí stránka | 44 | výpis, vyhledávání, blog | rádius 4 px |
| `--tool` | Přidat do porovnání (ikona) | `--icon --lg` 52 | detail | — |
| `--tool` | Zvětšit obrázek | `--icon` 44 | detail | — |
| `--neutral` | Pokračovat v nákupu, Celý sortiment | `--lg` 52 | popup, 404 | — |
| `--neutral` | Zavřít (křížek) | `--icon` 44 | popup košíku, megamenu, filtr | filtr rádius 4 px |
| `--light` | Akce, Cenově výhodné, Unikátní, Top produkty | 44 | sortiment | — |
| `--ghost` | Celý sortiment, Celá kategorie, Všechny novinky | 44 (mobil 52) | homepage karusely | rádius 4 px |
| `--ghost` | Zavřít (křížek, `primary-800`) | `--icon` 44 | modal přihlášení, modal prodejen | — |
| `--danger` | Odebrat z košíku (koš) | `--icon` 44 | košík | — |
| `--danger` | Zrušit vše | `--sm` 32, podtržené | výpis, filtr | — |
| `--danger-outline` | Zrušit filtry | `--lg` 52 | šuplík filtru | rádius 4 px |
| `--danger-outline` | Odebrat vše | 44 | porovnání | rámeček `secondary-200`, rádius 4 px |
| `--on-dark` | Zobrazit akci | `--lg` 52, písmo 17 | hero homepage | — |
| `--on-dark` | Prohlédnout nabídku, Číst dále, Zobrazit seznam | 44 | výpis (bannery), homepage | — |
| `--on-dark` | Zobrazit kategorii | `--field` 48 | sortiment | — |
| `--on-dark` | Nezávazná konzultace, Rychlá poptávka | `--lg` 52 | NZU (text `primary-800` / `nzu-green`) | — |
| `--on-dark-outline` | Spočítat spotřebu (hero), 608 308 078 | `--lg` 52 | homepage, NZU | — |
| `--on-dark-outline` | Kontakty a prodejny | `--field` 48 | detail článku | — |
| `--on-dark-outline` | Šipky hero | `--icon --field` 48, rámeček bílá 40 % | homepage | — |
| `--on-dark-outline` | Zpět k nákupu / do košíku / ke kontaktním údajům | `--xl` 64, rámeček bílá 45 % (mobil ikona 48) | košík krok 1–3 | — |

## Hlavička (vlastní třídy)

| Prvek | Třída | Velikost | Vzhled |
|---|---|---|---|
| Sortiment | `dsk-sortbtn` | 40 | `primary-300`, text `primary-900`, ikona mřížky + chevron |
| Porovnat, Přihlásit | `dsk-header-icon` | 48 | ikona 24 nad popiskem 700 13/16 bíle, počítadlo na rohu |
| Košík | `dsk-cartbtn` | 48 | `primary-800`, cena 700 16/20, počítadlo na rohu |
| Odkazy kategoriové lišty | `dsk-hdr-cat > a` | 56 | bílé 700 16/20, Služby a Články s chevronem (rozbalovací menu) |

## Prvky, které nejsou tlačítka

Číselník (`dsk-qty`, tlačítka −/+ bez podkladu `primary-800`), čipy filtrů (`dsk-chip` 32), dlaždice podkategorií (`dsk-ctile`), volby dopravy a platby (`dsk-opt`), kroky košíku (`dsk-step`), položky stromu kategorií a mobilního menu, odkazy rychlých kontaktů v patičce (`dsk-tile`) a plovoucí přepínač „Sekce“ (jen v prototypu).
