# Button

Všechna tlačítka e-shopu, definovaná třídami. Každé tlačítko = základ `dsk-btn` + **jedna role** + volitelně **velikost** a **tvar**. Rádius je vždy `radius-md` (6 px), šipka jednoduchý chevron, ikonové tlačítko má `aria-label`. Úplný soupis, kde se které tlačítko na stránkách používá, je v sekci **Tlačítka** a v kartě ButtonSurfaces.

## Role

| Třída | Výplň | Text / ikona | Rámeček | Hover | Pro co |
|---|---|---|---|---|---|
| `dsk-btn--conversion` | `main-500` | `primary-900` | — | `main-400`, stisk `main-600` | nákup a „zavolejte / přihlaste se“: Do košíku, Koupit, Přejít k objednávce, Pokračovat, AI asistent, Spočítat spotřebu, Poslat poptávku, Přihlásit (newsletter) |
| `dsk-btn--primary` | `primary-800` | bílá | — | `primary-700` | tmavá ovládací akce: Hledat, Filtrovat, Vybrat / Nastavit prodejnu, Více informací, Ověření dodavatelé, hamburger, vybraná záložka |
| `dsk-btn--secondary` | `primary-600` | bílá | — | `primary-700` | posun dál: Další (stránkování), Zobrazit 36 produktů (filtr), Na začátek stránky, Rychlá poptávka (služby) |
| `dsk-btn--soft` | bílá | `primary-700` | 1 px `primary-200` | `primary-50`, rámeček `primary-300` | jemné sekundární: Máte účet? Přihlaste se, Registrujte se, Kde řežeme, Zjistit více |
| `dsk-btn--outline` | bílá | `primary-600` | 2 px `primary-600` | `primary-50` | jediné tlusté obrysové: Načíst dalších 24 (48 px) |
| `dsk-btn--tool` | bílá | `primary-800` | 1 px `secondary-200` | `primary-50`, rámeček `primary-600` | nástroje a čísla: Přidat do porovnání, Zvětšit obrázek, Předchozí v karuselu, čísla stránek |
| `dsk-btn--neutral` | `secondary-100` | `primary-800` | — | `secondary-200` | návrat a zavření: Pokračovat v nákupu, Celý sortiment (404), křížek v popupu |
| `dsk-btn--light` | `primary-50` | `primary-600` | — | `primary-100` | rychlé výběry: Akce, Cenově výhodné, Unikátní, Top produkty |
| `dsk-btn--ghost` | průhledná | `primary-600` | — | `primary-50` | textová akce s chevronem: Celý sortiment, Celá kategorie, Všechny novinky; křížek v modalu (`primary-800`) |
| `dsk-btn--danger` | průhledná | `danger` | — | `secondary-50` | odebrání: koš v košíku, Zrušit vše (podtržené, 32 px) |
| `dsk-btn--danger-outline` | bílá | `danger` | 1 px `danger` | `secondary-50` | Zrušit filtry, Odebrat vše |
| `dsk-btn--on-dark` | bílá | `primary-700` | — | `primary-50` | hlavní akce na tmavé ploše: Zobrazit akci, Prohlédnout nabídku, Zobrazit kategorii, Číst dále |
| `dsk-btn--on-dark-outline` | průhledná | bílá | 1 px bílá 50 % (v liště košíku 45 %) | bílá 12 % | vedlejší akce na tmavé ploše: Spočítat spotřebu (hero), telefon (NZU), Kontakty a prodejny, Zpět v liště košíku, šipky hero |

## Velikosti

| Třída | Výška | Padding | Písmo | Kdy |
|---|---|---|---|---|
| `dsk-btn--sm` | 32 | 0 12 | 700 13/18 | Zrušit vše, čipy |
| *(výchozí)* | 44 | 0 16 | 700 15/20 | většina tlačítek, ikonová tlačítka, šipky karuselu, stránkování, záložky |
| `dsk-btn--field` | 48 | 0 16 | 700 15/20 | vedle pole 48 px (Hledat, newsletter), AI asistent, Spočítat spotřebu, Zobrazit kategorii, Načíst dalších 24 |
| `dsk-btn--lg` | 52 | 0 24 | 700 16/20 | hlavní akce: Koupit (18 px), Přejít k objednávce, Přihlásit se, hero, šipky karuselu na mobilu |
| `dsk-btn--xl` | 64 | 8 20 8 28 | dvouřádkový `dsk-btn__two` 20/24 + 14/18 | jen lišta košíku: Zpět, Pokračovat / Odeslat objednávku |

Tvar: `dsk-btn--icon` = čtverec (šířka = výška), `dsk-btn--joined` = bez rádiusu (Hledat přilepené k poli, rádius má jen vnější obal).

## Pravidla

- Na obrazovce je nejvýš jedna velká konverzní akce; ve výpisech se opakuje jen čtvercové Do košíku v kartě.
- Tlačítka vedle sebe mají stejnou výšku i roli velikosti (Koupit 52 + číselník 52 + porovnání 52).
- Na `primary-500` (hlavní lišta) stojí jen tmavé (`primary-800`) a konverzní tlačítko; na tmavých plochách jen `--on-dark`, `--on-dark-outline` a konverzní.
- Fokus: 3 px `primary-600`, odsazení 2 px. Neaktivní: 45 % krytí, `aria-disabled`.
