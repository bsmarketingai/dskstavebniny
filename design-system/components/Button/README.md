# Button

Všechna tlačítka e-shopu. Varianta říká roli akce, ne barvu. **Všechna mají `radius-md` (6 px)**, tlačítka vedle sebe mají stejnou výšku, šipka je vždy jednoduchý chevron.

| Třída | Kdy | Příklad na webu |
|---|---|---|
| `dsk-btn--conversion` | konverzní cesta a „zavolejte / přihlaste se k odběru“ | Do košíku, Koupit, Přejít k objednávce, Pokračovat, AI asistent, Přihlásit (newsletter), Spočítat spotřebu |
| `dsk-btn--primary` | tmavá ovládací akce (`primary-800`) | Hledat, Filtrovat, vybraná záložka, šipka Další v karuselu |
| `dsk-btn--secondary` | posun dál ve výpisu (`primary-600`) | Další ve stránkování |
| `dsk-btn--soft` | jemné sekundární: bílé, 1 px `primary-200`, text `primary-700` — nikdy tlusté 2 px obrysy | Máte účet? Přihlaste se, Registrujte se, Zpět (světlá lišta) |
| `dsk-btn--outline` | jediné 2 px obrysové, 48 px | Načíst dalších 24 |
| `dsk-btn--neutral` | návrat a zavření v popupu | Pokračovat v nákupu |
| `dsk-btn--ghost` | textový odkaz s chevronem, hover podklad `primary-50` | Celý sortiment, Celá kategorie, Všechny novinky |
| `dsk-btn--danger` | odebrání (text nebo ikona červeně) | Zrušit vše, koš v košíku |
| `dsk-btn--on-dark` | hlavní akce na tmavé ploše (bílé, text `primary-700`) | Zobrazit akci (hero), Prohlédnout nabídku, Zobrazit kategorii |
| `dsk-btn--on-dark-outline` | vedlejší akce na tmavé ploše (1 px bílá 50 %) | Spočítat spotřebu (hero), Zpět k nákupu (lišta košíku), telefon v NZU |

Výšky: `--sm` 32, výchozí 44, `--field` 48 (vedle pole), `--lg` 52, `--xl` 64 (lišta košíku); `--icon` = čtverec. Dvouřádkový popisek `dsk-btn__two` (Pokračovat / ke kontaktním údajům). Na obrazovce je nejvýš jedna velká konverzní akce. Ikonové tlačítko má vždy `aria-label`.

**Hover:** konverzní se zesvětlí na `main-400` (8,8:1), stisknuté `main-600`; tmavá zesvětlí o krok (`primary-700`); světlá dostanou `primary-50`. Hover nikdy nesnižuje kontrast. Fokus: 3 px `primary-600`, odsazení 2 px.
