# Konvence pojmenování komponent a CSS tříd — platforma BSSHOP

> Účel: instrukce pro Claude Design (CD), jak pojmenovávat nové komponenty, CSS třídy, ID a datové atributy tak, aby odpovídaly tomu, co reálně generuje platforma BSSHOP. Vše níže je odpozorováno přímo z živého HTML/CSS na **bigboy.cz** (homepage, výpis kategorie, detail produktu, 3 kroky košíku, vyhledávací a přihlašovací popup) — jde o skutečné, produkční vzory, ne o teoretický BEM/utility systém.

---

## 1. Základní vzorec kořenové třídy komponenty

Každá "serverová" komponenta (BSSHOP interně tomu říká View / Control) má na svém kořenovém elementu **stejné jméno jako ID**, plus třídu se sufixem `View`, plus sadu systémových tříd. Reálný příklad (dialog po přidání do košíku):

```html
<div id="BasketResultDialog"
     class="BasketResultDialogView v1a v1 bs-view dcon dc225 large BasketResultDialog bs-dialog bs-tab-boundary information">
```

Rozpad pořadí tříd, které CD by měl replikovat:

| Pozice | Příklad | Význam |
|---|---|---|
| 1 | `BasketResultDialogView` | **Styling třída** — `<NázevKomponenty>View`, PascalCase |
| 2 | `v1a v1` | **Look/varianta vzhledu** — viz kap. 5 |
| 3 | `bs-view` | Systémová třída platformy — označuje kořen libovolné View komponenty |
| 4 | `dcon dc225` | Infrastruktura CMS dynamických kontejnerů — **ignorovat**, viz kap. 8 |
| 5 | `large` | Volný modifikátor (velikost/varianta), holé slovo bez prefixu |
| 6 | `BasketResultDialog` | **JS/identifikační třída** — stejné jméno jako `id`, bez sufixu `View` |
| 7 | `bs-dialog`, `bs-tab-boundary`, `information` | Systémové/sémantické třídy (typ komponenty, focus-trap, typ obsahu) |

**Pravidlo pro CD:** nová komponenta = `id="Nazev"` + třídy `"NazevView <look-varianta> bs-view <modifikátory> Nazev"`. Dvojice `NazevView` (na styling) + `Nazev` (na JS/identifikaci) se opakuje úplně všude v systému — je to jediný pevný vzorec, který se nikdy neporušuje.

---

## 2. Prefix podle sekce webu (page/module namespace)

Komponenty specifické pro určitou stránku mají prefix podle stránky. Toto je nejdůležitější pravidlo pro konzistenci s BSSHOP — **nový komponent pro detail produktu musí mít prefix `PD`, ne generický název**.

| Prefix | Sekce | Reálné příklady z webu |
|---|---|---|
| `PD` | Detail produktu | `PDAddToCart`, `PDImages`, `PDAvailabilityPanel`, `PDDescription`, `PDProductReviewSummary`, `PDOptionalProducts`, `PDTable`, `PDInstallmentCalculator`, `PDLoyaltyProductInfo`, `PDSalesVoucher` |
| `Basket` | Obsah košíku (krok 1) | `BasketMaster`, `BasketTableRwd`, `BasketOptionalGifts`, `BasketXynActionsList`, `BasketLoyaltyInfo` |
| `Order` | Celý objednávkový flow (kroky 1–3) | `OrderMaster`, `OrderNavigator`, `OrderActionPanelHorizontal`, `OrderValidationResult`, `OrderBillingForm1`, `OrderRegistrationFormView` |
| `Home` | Homepage | `HomeArticle(s)`, `HomeHeading`, `HomeProduct(s)` — stránka samotná se jmenuje `EshopHome` / `EshopHomeView` |
| *(bez prefixu)* | Globální layout (header, footer, napříč stránkami) | `Header`, `Footer`, `Logo`, `MenuCategories`, `SimpleSearch`, `SimpleBasket`, `LoginUser`, `Contacts` |

Vzorec: **`<PagePrefix><PopisnýNázev>`**, PascalCase, bez podtržítek a pomlček.

### Stav stránky na `<body>`

```html
<body class="ProductDetailState cz anonymous eid1071">   <!-- detail produktu -->
<body class="EshopHomeState cz anonymous eid1071">        <!-- homepage -->
<body class="BasketState ...">                            <!-- košík -->
```

Vzorec: `<NázevStránky>State` + kód lokalizace (`cz`/`sk`) + stav přihlášení (`anonymous`) + interní ID entity (`eid…`, needs no imitace).

---

## 3. Vnitřní (element) třídy — camelCase, žádné BEM

BSSHOP **nepoužívá BEM** (`block__element--modifier`). Vnitřní části komponenty se pojmenovávají prostým **camelCase řetězením** názvu bloku a části, bez oddělovače:

Reálný příklad — widget "doprava zdarma" v dialogu:

```html
<div class="freeDeliveryProgress">
  <div class="freeDeliveryProgressTrack">
    <div class="freeDeliveryProgressFill"></div>
    <span class="freeDeliveryProgressMarker">
      <span class="freeDeliveryProgressMarkerLabel">999 Kč</span>
    </span>
  </div>
</div>
```

Další reálné příklady stejného principu: `priceDetailWrap`, `imageNameWrapper`, `productDetailUsp`, `deliveryPricesSummaryWrap`, `numberWrap`, `stepSeparator`.

**Pravidlo pro CD:** když modeluješ vnitřní části nové komponenty `Xyz`, pojmenuj je `xyzHeader`, `xyzBody`, `xyzTrack` apod. — ne `Xyz__header` a ne `xyz-header`.

---

## 4. Wrapper konvence

Obalové elementy se značí suffixem/slovem "Wrap", ne generickým `container`:

- `...Wrap` — `priceWrapCustom`, `deliveryPricesSummaryWrap`, `basketSummaryWrap`, `footerSubsWrap`, `uspWrap`, `goTopWrap`
- `...WrapInner` — `LoginWrapInner`
- samostatná třída `outer` na obalovém `<div>` — např. `<div class="textBox outer"><input class="textBox ..."></div>` (input i obal sdílejí základní jméno komponenty, obal má navíc `outer`)

---

## 5. Look/varianta vzhledu (`v1`, `v1a`, `v2`, …)

Skoro každá komponenta nese dvojici tříd `vN vNa` (např. `v1 v1a`, `v2 v2a`, `v5 v5a`). Je to vizuální varianta řízená z administrace BSSHOP (odpovídá atributu `data-look` v HTML, který se objevuje ~229× na stránce). Číslo/písmeno nemá sémantický význam samo o sobě — je to jen "sloupec" v systému vzhledů.

**Pravidlo pro CD:** tyto třídy se **negenerují ručně** pro nový komponent — nejsou to sémantické názvy, jsou to čísla verzí vzhledu přiřazená administrátorem. CD je nemá vymýšlet ani napodobovat, jen vědět, že v reálném markupu tam budou.

---

## 6. Systémové (frameworkové) třídy s prefixem `bs-`

Prefix **`bs-` je rezervovaný pro jádro platformy BSSHOP** (session engine, ne pro konkrétní projekt/klienta). CD **nesmí vymýšlet nové `bs-*` třídy** — pouze používat existující, pokud modeluje chování, které do dané kategorie spadá:

| Třída | Kde se používá | Význam |
|---|---|---|
| `bs-view` | kořen úplně každé View komponenty | univerzální marker "toto je BSSHOP komponenta" |
| `bs-dialog` | vystředěný modál (např. potvrzení přidání do košíku) | typ overlaye: centered dialog |
| `bs-dialog-overlay` | pozadí/backdrop centered dialogu | — |
| `bs-popup-open` | trigger element kontextového popupu (přihlášení, vyhledávání) | popup je aktuálně otevřený |
| `bs-popup-overlay` | pozadí kontextového popupu | typ overlaye: anchored popup (ne centered) |
| `bs-tab-boundary` | kořen jakéhokoli focus-trapped panelu (dialog i popup) | accessibility — hranice pro Tab/Shift+Tab |
| `bs-error-hint`, `bs-error-hint-target` | validace formulářů | bublina s chybovou hláškou u pole |
| `bs-crv` | dekorativní "vlnky" v headeru/footeru | okrajový tvar (curve) |
| `bs-priceLayout` | cenové bloky | layout ceny (základní cena / cena s DPH / sleva) |
| `bs-spacer{N}` | např. `bs-spacer20` | utility mezera o `{N}`px |

**Rozlišení dialog vs. popup je důležité:** vystředěné modální okno (potvrzení akce) → `bs-dialog` + `bs-dialog-overlay`. Kontextově ukotvené okno u prvku (přihlášení, vyhledávání) → `bs-popup-open`/`bs-popup-overlay`, kořen má navíc jen bare třídu `popup`. Obojí má `bs-tab-boundary`.

---

## 7. Stavové třídy — holá slova, ne BEM modifikátory

Stav se značí prostým anglickým slovem přidaným do `class`, ne `is-` prefixem ani `--modifikátorem`:

```html
<div class="step step0 active">...</div>
<div class="step step1 inactive">...</div>
```

Další pozorované stavové/booleovské třídy: `active` / `inactive`, `selected`, `disabled`, `expanded`, `visible`, `required`, `empty`, `floating`, `nop` (needs no pointer — needs no click, typ. na už navštívený krok).

**Pravidlo pro CD:** stav vždy jako samostatné anglické slovo (`active`, `disabled`, `expanded`…), nikdy `is-active` nebo `Component--active`.

---

## 8. Krokový wizard (Order flow) — konkrétní referenční vzor

Přesný markup indikátoru kroků z `/objednat-krok1/` (3kroková objednávka: Obsah košíku → Kontaktní údaje → Kontrola údajů):

```html
<div id="OrderNavigator" class="OrderNavigatorView v2a v2 bs-view steps3 dcon dc313 OrderNavigator">
  <div class="steps">
    <div class="step step0 active">
      <a class="linkname nop"><span class="name">Obsah košíku</span></a>
      <a class="numberWrap nop"><span class="number">1</span></a>
    </div>
    <div class="stepSeparator"><span></span></div>
    <div class="step step1 inactive">
      <a class="linkname"><span class="name">Kontaktní údaje</span></a>
      <a class="numberWrap"><span class="number">2</span></a>
    </div>
    <div class="stepSeparator"><span></span></div>
    <div class="step step2 inactive">…</div>
  </div>
</div>
```

URL kroků: `/objednat-krok1/`, `/objednat-krok2/`, `/objednat-krok3/` — vzorec `objednat-krok{N}`.

**Pravidlo pro CD:** libovolný vícekrokový proces (ne jen checkout) modeluj stejně — `steps` → `step step{N} active|inactive` → `stepSeparator`, číslované od nuly.

---

## 9. Formuláře — konvence "Smartform"

Vstupní pole v BSSHOP mají dvouúrovňové pojmenování — obecný typ pole + instance v konkrétním formuláři:

```html
<input class="textBox xta_firstName bs-error-hint-target error">
```

Pozorované třídy: `smartform-email`, `smartform-phone-number`, `smartform-instance-billing-email`, `smartform-instance-billing-phone`, `smartform-instance-contact`. Formulářové kontejnery: `OrderBillingForm1`, `OrderCompanyForm`, `OrderUserForm`, `OrderRegistrationFormView`.

**Pravidlo pro CD:** nové pole pojmenuj `smartform-<typ pole>` (obecně) a při potřebě rozlišit kontext formuláře přidej `smartform-instance-<kontext>-<pole>` (např. `smartform-instance-shipping-email`). Chybová bublina u pole vždy přes `bs-error-hint-target` (na inputu) + `bs-error-hint` (na bublině), stav chyby navíc jako holé slovo `error` (viz kap. 7).

---

## 10. Design tokeny (CSS proměnné)

227 CSS custom properties na `:root`, jasný a opakovatelný vzorec **kebab-case**: `--<oblast/komponenta>-<varianta>-<vlastnost>`.

```css
--main-button-text-color
--main-button-gradient-top-color
--neutral-button-border-color
--secondary-button-gradient-bottom-color
--inbasket-button-border-color

--actionIcon-new-color
--actionIcon-new-text-color
--actionIcon-discount-color
--actionIcon-freeShipping-text-color

--menu-level-color-1 … --menu-level-color-9
--menu-level-text-color-0 … --menu-level-text-color-9

--bg-color / --bg-header-color / --bg-popup-color / --bg-content-color
--text-color / --text-on-primary-color / --text-weaker-color
--border-radius / --input-border-radius / --popup-border-radius
--bs-header-height / --bs-max-popup-height   (jediné dva "bs-" tokeny — layoutová geometrie, ne barvy)
```

Vzor pro tlačítka je obzvlášť pravidelný a hodí se jako šablona pro cokoliv "variantového" (badge, ikona akce apod.):

`--<varianta>-button-color`, `--<varianta>-button-text-color`, `--<varianta>-button-border`, `--<varianta>-button-border-color`, `--<varianta>-button-border-width`, `--<varianta>-button-gradient`, `--<varianta>-button-gradient-top-color`, `--<varianta>-button-gradient-bottom-color`

kde `<varianta>` ∈ `main`, `neutral`, `secondary`, `inbasket`.

**Pravidlo pro CD:** nový token vždy kebab-case, začni obecnou oblastí/komponentou, pokračuj variantou/stavem, skonči vlastností (`-color`, `-text-color`, `-border-radius`…). Prefix `bs-` u tokenů nepoužívat (rezervováno pro 2 layoutové konstanty platformy).

---

## 11. Odznaky a badge produktů

Product card štítky (viděno na homepage/kategorii: "Tip na dárek", "-25 %", "Doporučujeme", "Novinka", procento hodnocení) odpovídají třídám `flag02`, `flag12`, `flag14`…`flag18` a CSS proměnným `--actionIcon-<typ>-color` / `--actionIcon-<typ>-text-color`, kde `<typ>` je `new`, `sale`, `discount`, `top`, `gift`, `recommended`, `freeShipping`, `bazar`, `xynaction`.

**Pravidlo pro CD:** nový typ odznaku pojmenuj jako další `--actionIcon-<novýTyp>-color` pár, ne jako samostatný systém.

---

## 12. Responzivní varianty — sufix `Rwd`

Komponenta, která má samostatnou (přestavěnou, ne jen media-query zúženou) mobilní/responzivní verzi, dostává sufix **`Rwd`** (Responsive Web Design):

`BasketTableRwd`, `CategoriesRwdView`, `MenuCategoriesRwdView`, `OrderActionPanelRwdView`, `FlatCategoriesRwdView`, `RwdTemplateView`.

**Pravidlo pro CD:** pokud komponenta potřebuje strukturálně odlišnou (ne jen CSS) verzi pro menší breakpointy, pojmenuj ji `<Nazev>Rwd` / `<Nazev>RwdView`, ne `<Nazev>Mobile`.

Konkrétní hraniční hodnoty breakpointů platformy (420/550/820/1000/1150/1440 px) jsou zdokumentované v `bsshop-breakpoints.md` — layout `PD`/`ProductCard` komponent se na ně přímo váže (práh 1000 a 1150 px odpovídá schváleným layoutům B/A).

---

## 13. Analytické/JS hooky — nikdy nestylovat na nich

Třídy s prefixem **`xta_`** jsou hooky pro trackování (Google Analytics / Ecommerce), ne stylovací třídy: `xta_addToCart`, `xta_addToCart_10218` (s ID produktu), `xta_quantity`, `xta_nextStep`, `xta_order`, `xta_firstName`, `xta_login`.

**Pravidlo pro CD:** nikdy nenavrhuj vzhled komponenty navázaný na `xta_*` třídu. Pokud nový komponent potřebuje trackovací hook, přidej `xta_<akce>` **navíc** k standardní `NazevView`/`Nazev` dvojici, nikdy místo ní.

---

## 14. CMS "dynamic container" infrastruktura — ignorovat při navrhování

Na stránce se objevuje velké množství tříd/ID, které **nejsou součástí designového systému** a CD by je neměl napodobovat ani se jimi inspirovat coby vzor pojmenování — jde o interní CMS instalatéry obsahu:

- vlastní HTML elementy `<dc-root>` a `<dc-con>` (Dynamic Container) obalující editovatelný obsah
- třída `dcon` + číslo instance `dc<N>` (např. `dc117`, `dc225`) — každý editovatelný blok má jiné číslo
- náhodná ID typu `e4032758` na needitovatelných/generovaných uzlech
- třídy typu `val_<hodnota>` — automaticky generované z hodnot atributových filtrů (např. `val_vegan`, `val_bez_lepku`)
- CSS bundly `combined_cont0_(min-width:…)and(max-width:…)` — to je infrastruktura pro načítání breakpointů (viz `bsshop-breakpoints.md`), ne komponenta

**Pravidlo pro CD:** tohle je "šum" generovaný CMS a builderem stránek. Nový komponent nikdy nepojmenovávej podle `dcNNN` ani `eNNNNNNN` vzoru — drž se sémantických PascalCase názvů z kapitol 1–2.

---

## 15. Datové atributy (`data-*`)

Pozorováno na produkci: `data-lazy` + `data-src` (lazy-loading obrázků), `data-cat-id` (ID kategorie), `data-look` (číslo vizuální varianty, viz kap. 5), `data-name` (název produktu pro GA), `data-type`, `data-value`, `data-place-token` / `data-place-view` (reklamní/bannerové sloty), `data-pageid`.

**Pravidlo pro CD:** chování (ne vzhled!) navazuj na `data-*` atributy, ne na třídy — např. `data-place-token` pro reklamní sloty, `data-cat-id` pro filtrování. Styling zůstává vždy na třídách z kapitol 1–7.

---

## 16. Rychlý checklist pro Claude Design

Při návrhu nového komponentu pro BSSHOP:

1. Urči **prefix sekce** (`PD`, `Basket`, `Order`, `Home`, nebo bez prefixu pro globální layout).
2. Kořenový element: `id="<Prefix><Nazev>"` + třídy `"<Prefix><Nazev>View bs-view <Prefix><Nazev>"`.
3. Vnitřní části: `camelCase` řetězení, **bez** `__`/`--` (BEM zakázán).
4. Obal: `...Wrap` / `...WrapInner`, nebo bare třída `outer` vedle základního jména.
5. Stav: holé anglické slovo (`active`, `disabled`, `expanded`…), ne `is-*`.
6. Overlay/modal: vystředěný → `bs-dialog`/`bs-dialog-overlay`; ukotvený u prvku → `bs-popup-open`/`bs-popup-overlay`; obojí + `bs-tab-boundary`.
7. Formulářové pole: `smartform-<typ>` (+ `smartform-instance-<kontext>-<pole>` když je potřeba rozlišit formulář).
8. Nový design token: kebab-case `--<oblast>-<varianta>-<vlastnost>`, žádný nový `bs-*` token.
9. Trackovací hook navíc, nikdy místo stylovací třídy: `xta_<akce>`.
10. Nikdy nenapodobovat `dcNNN` / `eNNNNNNN` / `val_*` — to je CMS šum, ne vzor k replikaci.
11. Potřebuje-li komponenta strukturálně jinou mobilní verzi → `<Nazev>Rwd`.

---

## 17. Mapování na DSK design systém

Tokeny design systému jsou škály (`primary-500`, `main-500`…); v BSSHOP šabloně se mapují na sémantické proměnné platformy:

| BSSHOP proměnná | DSK token |
| --- | --- |
| `--main-button-color` / `--main-button-text-color` | `conversion` (`main-500`) / `conversion-ink` (`primary-900`) |
| `--inbasket-button-color` | `conversion` |
| `--secondary-button-color` / `-text-color` | `primary-800` / `white` |
| `--neutral-button-color` / `-text-color` | `secondary-100` / `primary-800` |
| `--bg-color` / `--bg-content-color` | `white` |
| `--bg-header-color` | `primary-500` |
| `--bg-popup-color` | `white` |
| `--text-color` / `--text-weaker-color` | `secondary-900` / `secondary-600` |
| `--text-on-primary-color` | `primary-900` (na `primary-500` nikdy bílá) |
| `--actionIcon-sale-color` | `danger` |
| `--actionIcon-new-color` | `primary-800` |
| `--actionIcon-discount-color` | `danger` |
| `--border-radius` / `--input-border-radius` / `--popup-border-radius` | `radius-md` 6 / `radius-sm` 4 / `radius-lg` 8 |
| `--menu-level-color-1…` | `primary-800`, `primary-600`, `primary-100`, `white` |

Komponenty na plátně už nesou BSSHOP názvy tam, kde je platforma zná: `MenuCategories`, `MenuCategoriesMega`, `SimpleSearch`, `SimpleBasket`, `LoginUser`, `Footer`, `PDImages`, `PDAddToCart`, `PDAvailabilityPanel`, `PDDescription`, `BasketResultDialog` (+ `bs-dialog bs-tab-boundary`, vnitřek `freeDeliveryProgress`, `freeDeliveryProgressTrack`, `freeDeliveryProgressFill`).
