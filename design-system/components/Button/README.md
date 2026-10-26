# Button

Všechna tlačítka e-shopu. Varianta říká, jakou roli akce má, ne jakou má barvu.

| Třída | Kdy |
|---|---|
| `dsk-btn--conversion` | jen konverzní cesta: Do košíku, Koupit, Přejít k objednávce, AI asistent |
| `dsk-btn--primary` | hlavní nekonverzní akce: Hledat, Přihlásit k odběru, Nastavit jako svoji prodejnu, Filtrovat |
| `dsk-btn--secondary` | potvrzení v panelu: Zobrazit 128 produktů |
| `dsk-btn--neutral` | návrat a zavření: Pokračovat v nákupu, ikona zavřít |
| `dsk-btn--outline` | doplňková akce na bílé: Načíst dalších 24 |
| `dsk-btn--danger` | mazání: Zrušit filtry |
| `dsk-btn--ghost` | textová akce s ikonou: Info o prodejně, Celý popis |

Velikosti `--sm` 32, výchozí 44, `--lg` 52 px; `--icon` = čtverec. Na obrazovce je nejvýš jedna velká konverzní akce. Ikonové tlačítko má vždy `aria-label`.

**Hover:** konverzní se zesvětlí (`main-400`, kontrast 8,8:1), stisknuté ztmavne (`main-600`); tmavá tlačítka zesvětlí o krok (`primary-700`); světlá a obrysová dostanou podklad `primary-50`. Hover nikdy nesnižuje kontrast textu. Na plátně jsou hovery zapsané atributem `style-hover`.