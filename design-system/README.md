# DSK Stavebniny

Design systém pro redesign e-shopu dskstavebniny.cz. **Srovnaný s finálními stránkami redesignu 27. 10. 2026** (homepage, sortiment, kategorie, detail, vyhledávání, porovnání, košík ve 3 krocích, kontakty, poptávka, dodavatelé, blog, služby NZU a Řezání oceli, 404 a všechny vrstvy). Kde se stránky a systém lišily, platí stránky; rozpory, které stojí za sjednocení na webu, jsou v sekci Audit.

Rozsahy breakpointů XXS–XXL a maximální šíře (1560 px obsahu) jsou v sekci Breakpointy, rozestupy a výšky prvků v sekci Rozestupy. Pojmenování podle platformy BSSHOP je v sekci Pojmenování, informační architektura e-shopu v sekci Struktura.

## Hlas a obsah

Mluvíme jako zkušený prodavač na prodejně: věcně, česky, bez marketingových frází. Vykáme. Tlačítka říkají přesně, co se stane — „Do košíku“, „Pokračovat ke kontaktním údajům“, „Zobrazit všechny produkty“, nikdy „Odeslat“ nebo „OK“. Čísla píšeme s nezlomitelnou mezerou (42 000 produktů, 220,58 Kč). Cena je vždy s DPH velkým písmem a pod ní cena bez DPH — řada zákazníků jsou firmy. Skladovost vždy dvěma řádky: vybraná prodejna a součet na 9 prodejnách.

## Vizuální základ

**Barva.** Paleta je z Figma stylů: škály `main` (oranžová), `primary` (modrá), `secondary` (modrošedá) a `neutral`. Hlavička má tři pásy: utility lišta `primary-900`, hlavní lišta `primary-500` (DSK modrá — malý text na ní `primary-900`, bílá jen logo a popisky ikon), kategoriová lišta `primary-600` s bílými odkazy a tlačítkem Sortiment na `primary-300`. Tmavé plochy: `primary-900` (hero, patička, karty hlavních kategorií, banner kalkulačky) a `primary-800` (ovládací tmavé prvky, newsletterový box, promo bannery, plovoucí lišta košíku). Nadpisy a ceny `primary-700`, odkazy a ghost tlačítka `primary-600`, světlé pásy `primary-50`, tinty a fokus `primary-100`.

`main` je **konverzní barva** (`conversion` = `main-500`, hover `main-400`, text `conversion-ink` = `primary-900`, nikdy bílý): Do košíku, Koupit, Přejít k objednávce, Pokračovat v košíku, AI asistent. Dál ji smíme použít jen tam, kde vede ke kontaktu nebo odběru — telefony v patičce, Přihlásit k odběru newsletteru, kalkulačka spotřeby, počítadla a štítek kampaně v hero. Nic jiného oranžové není. Stavové barvy mimo Figma škály: `danger` (Výprodej, přeškrtnutá cena, Zrušit vše, koš, povinné pole) a `success` (skladem, Zdarma, Otevřeno). `nzu-green` patří jen stránce Nová zelená úsporám (barva z banneru programu).

**Typografie.** Jedna rodina `Exo 2`. **Nejtěžší řez je Bold (700)** — ExtraBold ani Black nepoužíváme. H1 40/44 (detail 36/42, mobil 28/34), H2 28/34 (mobil 22/28), nadpis bloku 24/30, nadpis v banneru 22/28, hero 56/60. Nadpisy, navigace, tlačítka a ceny 600–700, text 400–500. Hierarchii nese velikost. Verzálky jen u popisku „KROK 1“ v košíku.

**Bez dekorací.** Žádné linky ani „metr“ pod nadpisy. Jediný doplněk nadpisu je **ikona ve čtverci** 44 × 44 px, `radius-md`, podklad `primary-700`, bílá ikona (Časté dotazy, Způsob dopravy, karty formuláře, sekce služeb, dialogy).

**Tvar.** `radius-sm` 4 px — pole, výběr, čipy, štítky, číselník, stránkování. `radius-md` 6 px — **všechna tlačítka**, ikony u nadpisů, karty produktů, dlaždice, volby, kroky košíku. `radius-lg` 8 px — bannery, karty kategorií, karta formuláře, tabulka, dialogy. Vnořený prvek přilepený k okraji rodiče přebírá jeho rádius (číslo kroku 5 0 0 5 v kroku s 6 px). Kulaté jsou jen počítadla a stavové tečky. Karty bez stínu; stín jen plovoucí vrstvy (`shadow-pop`), lišta košíku (`shadow-bar`), toast a karta při hoveru.

**Tlačítka.** Role, ne barvy — definice tříd v kartě Button, použití podle podkladu v kartě ButtonSurfaces a úplný soupis v sekci Tlačítka. Sekundární tlačítka jsou **jemná**: bílá, 1 px `primary-200`, text `primary-700` — tlusté 2 px obrysy jen u „Načíst dalších 24“. Tlačítka vedle sebe mají stejnou výšku. Šipky jsou vždy jednoduchý chevron.

**Formuláře.** Popisek nad polem, pole 48 px, rámeček `secondary-400`, `radius-sm`; fokus = rámeček `primary-600` + prstenec 3 px `primary-100`.

**Rozestupy.** Škála na 4 px; okraj, gutter, mezera sekcí, padding pásů a karet jsou responzivní proměnné (sekce Rozestupy).

## Skladba stránky

Hlavička → drobečky (13/18) → H1 → obsah → **Časté dotazy** (pás `primary-50`) → **newsletter** → patička. Výjimky: 404 (bez FAQ a newsletteru) a košík (bez FAQ, newsletteru i patičky — posledním prvkem je plovoucí lišta). Používáme hotové komponenty z jiných stránek: produktová karta je vždy `pcard`, karusely mají stejnou navigaci, stránkování a dlaždice podkategorií jsou jako ve výpisu kategorie, přepínač sekcí jako panel „Sekce“. Na mobilu nic horizontálně neroluje kromě karuselů (ty jdou až k okraji); seznamy a tabulky se skládají do karet. Hover na mobilu nefunguje — vše musí jít kliknutím (mini košík se na mobilu otevírá klepnutím).

## Ikonografie

Sada **Tabler Icons** (outline) v3.24.0, MIT. 20 px v UI, 24 px v hlavičce a ve čtverci u nadpisu, 16 px ve štítcích a skladovosti; `stroke-width` 1.75 (check 2.25–2.5); `currentColor`, inline SVG. Šipky v tlačítkách, odkazech a karuselech vždy `chevron-right` / `chevron-left`. Vlastní ikony: AI asistent `assets/Icons/ai-asistent.svg`, šroub `assets/Icons/sroub.svg` (Kotvení a spojování). Mapování kategorií: Stavebniny `wall`, Cenově výhodné `pig-money`, Nářadí `hammer`, Stavební chemie `flask`, Barvy a nátěry `paint`, Bydlení a zahrada `plant`, Pracovní oděvy `shirt`, Poukazy `gift`, Výprodej `tag` (červeně).

## Logo

`assets/Logo/logo-dsk-white.png` — bílé logo od klienta s průhledným pozadím (324 × 132 px). Jen na `primary-500` a tmavších modrých; v hlavičce 44 px (mobil 36 px). Ochranná zóna aspoň výška písmen „STAVEBNINY“. Barevná verze a SVG zatím chybí.

## Komponenty

Třídy v `components/bundle.css` (prefix `dsk-`, jen tokeny) a karta s ukázkou ke každé:

- **Základ:** Button, ButtonSurfaces, Badge, FormControls
- **E-shop:** ProductCard, Stock (skladovost), PriceStock (cena), QuantityStepper, CategoryTile
- **Košík:** CheckoutSteps, OptionList, CartBar, FormCard
- **Obsah:** SectionHeading, PromoBanner, DataTable, Faq, Newsletter, Usp
- **Zpětná vazba:** Notice, InfoBars, Toast
- **Navigace a hlavička:** HeaderActions, Dropdown, Navigation, Accordion
- **Vrstvy a patička:** Dialog, FooterTiles

Na stránkách prototypu mají komponenty vlastní krátké třídy (`pcard`, `stk`, `ko-*`, `kf-*`, `fq`, `nl`…); mapování je v kartách a v sekci Audit.
