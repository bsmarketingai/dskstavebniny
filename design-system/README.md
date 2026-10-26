# DSK Stavebniny

Design systém pro redesign e-shopu dskstavebniny.cz (dříve „Design System“). Rozsahy breakpointů XXS–XXL a maximální šíře webu (1560 px obsahu) jsou v sekci Breakpointy. Pojmenování komponent, tříd a tokenů podle platformy BSSHOP je v sekci Pojmenování (naming), informační architektura e-shopu v sekci Struktura. Vychází ze současné barevnosti webu (DSK modrá, tmavě modrá patička, oranžové nákupní akce) a zpřísňuje ji tak, aby všechny texty splnily kontrast WCAG AA.

## Hlas a obsah

Mluvíme jako zkušený prodavač na prodejně: věcně, česky, bez marketingových frází. Tykat ne, vykat ano. Tlačítka říkají přesně, co se stane — „Do košíku“, „Přejít k objednávce“, „Zobrazit 128 produktů“, nikdy „Odeslat“ nebo „OK“. Čísla píšeme s nezlomitelnou mezerou (42 000 produktů, 220,58 Kč). Cenu vždy uvádíme s DPH velkým písmem a pod ní cenu bez DPH (`caption`, `secondary-600`) — řada zákazníků jsou firmy.

## Vizuální základ

**Barva.** Paleta je převzatá 1:1 z Figma stylů: škály `main` (oranžová), `primary` (modrá), `secondary` (modrošedá) a `neutral` (šedá), každá 50–900. `primary-500` je identita: velké plochy (hlavní lišta, newsletter). Malý text na ní je vždy `primary-900` (5,4:1); bílá je na ní jen logo (3,0:1 neprochází). Tlačítka a odkazy s bílým textem `primary-600` (4,6:1), nadpisy a ceny `primary-700`, tmavé plochy (kategoriová lišta, patička, Hledat, košík) `primary-800`, utility lišta `primary-900`. Tint `primary-100`, podklad sekcí `primary-50`. `main` je **konverzní barva** (token `conversion` = `main-500`, hover `conversion-hover` = `main-600`, text `conversion-ink` = `primary-900`, nikdy bílý). Patří jen na konverzní cestu: Do košíku, Koupit, Přejít k objednávce, tlačítka pokladny a AI asistent, který stojí přímo u vyhledávání (vede k výběru a nákupu, chceme ho zviditelnit). Košík v hlavičce je tmavý (`primary-800`, bílý text) s oranžovým počítadlem; Porovnat a účet jsou bílé dlaždice s ikonou a textem `primary-800`. Na `primary-500` tak všechny ovládací prvky hlavičky stojí na bílé nebo tmavé ploše s kontrastem 11,6:1, nikdy přímo na modré. V patičce (tmavé `primary-900`) je podle návrhu oranžová i pro telefonní čísla, ikony kontaktů, otevírací dobu a odkazy v textu Doprava — tam funguje jako „zavolejte / zastavte se“, tedy také konverze. Všechna počítadla a notifikace (košík, porovnání, počet aktivních filtrů) jsou jednotně `main-500` s textem `primary-900`, kulatá, výška 20 px, písmo 11 px tučně. Nic jiného oranžové není — štítky akcí, ikony v patičce ani fokus. Díky tomu oko na každé stránce okamžitě najde další krok k nákupu. Text a UI ze škály `secondary`: text `secondary-900`, popisky `secondary-600`, hairline `secondary-200`, šedé podklady `secondary-100`. Červená `danger` a zelená `success` ve Figma paletě nejsou, držíme je jako stavové barvy mimo škály. Pozor: `main-50` je ve Figmě zelený a `secondary-50` růžový — používáme je jako podklad úspěchu a chyby, ale chce to ověřit. Přechodové styly `neutral 100-0` a `1000-0` (do průhledna) nejsou tokeny, řeší se v CSS jako gradient.

**Typografie.** Jedna rodina pro celý web: `Exo 2`, kterou web už používá. **Nejtěžší řez je Bold (700) — ExtraBold (800) ani Black (900) nepoužíváme, ani na nadpisy a ceny.** Nadpisy, navigace, tlačítka a ceny ve vahách 600–700 (`display`), odstavce a popisy 400–500 (`body`). Hierarchii nese velikost, ne extra tučný řez.

**Bez dekorací.** Systém nepoužívá žádné dekorativní prvky — žádné linky, metr ani ornamenty pod nadpisy. Hierarchii nese typografie, barva a rozestupy.

**Tvar.** Rádiusy jen v rozmezí 4–8 px, spíš menší: `radius-sm` (4 px) pro ovládací prvky, štítky a čipy, `radius-md` (6 px) pro karty a dlaždice, `radius-lg` (8 px) pro hero a plovoucí vrstvy. Vnořený prvek má vždy menší rádius než jeho rodič. Plně kulaté (`radius-round`) jsou jen počítadla a stavové tečky. **Kulatá tlačítka nepoužíváme nikde** — ani ikonová (šipky karuselů, šipky v kartách, hero); mají stejný rádius jako ostatní tlačítka. Karty nemají stín, odděluje je `secondary-200`; `shadow-pop` mají jen plovoucí vrstvy.

**Rozestupy.** Škála na 4 px (2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80), nic mimo ni. Okraj stránky, gutter, mezera mezi sekcemi, padding pásů a karet jsou responzivní proměnné — tabulka a pravidlo blízkosti v sekci Rozestupy.

## Ikonografie

Sada **Tabler Icons** (outline), verze **v3.24.0** z github.com/tabler/tabler-icons, MIT. Velikost 20 px v UI, 24 px v hlavičce, 16 px ve štítcích; `stroke-width` 1.75; barva `currentColor`. Ikony vkládáme jako inline SVG, aby přebíraly barvu textu. **Šipky:** v tlačítkách, odkazech a karuselech používáme vždy chevrony (`chevron-right`, `chevron-left`), nikdy `arrow-right` / `arrow-left`. Výjimka: tlačítko AI asistent má vlastní ikonu `assets/Icons/ai-asistent.svg` (bublina s jiskrami, dodaná klientem), převedenou na `currentColor`; v tlačítku 22 px, tah 2. Mapování hlavních kategorií e-shopu: Stavebniny `wall`, Cenově výhodné produkty `pig-money`, Kotvení a spojování vlastní šroub `assets/Icons/sroub.svg` (Tabler šroub nemá), Nářadí `hammer`, Stavební chemie `flask`, Barvy a nátěry `paint`, Bydlení a zahrada `plant`, Pracovní oděvy a obuv `shirt`, Poukazy `gift`, Výprodej `tag` (červeně).

## Logo

`assets/Logo/logo-dsk-white.png` — originální bílé logo od klienta s průhledným pozadím (324 × 132 px, ořezané na obrys). Používá se jen na `primary-500` nebo tmavších modrých; v hlavičce ve výšce 44 px. Ochranná zóna kolem loga je aspoň výška písmen „STAVEBNINY“. Barevná verze na bílé a vektor (SVG) zatím chybí.

## Komponenty (zatím popsané v návrhu, ne v kódu)

Hlavička (utility lišta / hlavní lišta / kategoriová lišta), megamenu, karta produktu, dlaždice kategorie, štítky (Výprodej, Novinka, Akce), skladovost, množství + Do košíku, drobečková navigace, šuplík filtru, popup Vložili jste do košíku, karta prodejny, patička.


---

## Consuming this system (generated — do not edit)

Every path named below is under `project/` in this design system: read `project/api/tokens.md`, not `api/tokens.md`.

This system ships tokens and assets, no components: take colours, type and fonts from the tokens card below for any page, deck or mock-up; a Slides deck or Design canvas also takes `tokens.json` by file path (that type’s SKILL.md says how).

**Read, per thing:** token values: `api/tokens.md`; stored assets and their paths: `api/assets/<Group>.md`. After this README, fetch the cards and fonts you need in ONE message as parallel calls — none depends on another.

**Two rules.** Before you use a thing — a component, a token group, an icon, an asset — read its card from the index below; a value you did not read from a card is a guess. `tokens.json`, `manifest.json` and `design-system.json` are sources for tools: hand them over. `SKILL.md` and `artifact-type/` beside them are authoring guidance, not needed to consume the system.

## Index (generated — do not edit)

**Tokens**

- `api/tokens.md` — Every token: palette, type, spacing, radius, shadow, breakpoint, size. (6.6k)

**Icons and assets**

- `api/assets/Logo.md` — 1 file, by asset id. (0.7k)
- `api/assets/Icons.md` — 1 file, by asset id. (0.7k)
- `api/assets/Other.md` — 20 files, by asset id. (2.0k)
