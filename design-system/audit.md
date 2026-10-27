# Audit komponent

Srovnání design systému s finálními stránkami redesignu (stav 27. 10. 2026): 18 stránek + 8 vrstev. Hodnoty byly změřeny na vykreslených stránkách (computed styles), ne odhadnuty.

## Co se v systému změnilo podle stránek

| Oblast | Dříve v systému | Na stránkách (platí) |
| --- | --- | --- |
| Rádius tlačítek | 4 px | **6 px** (`radius-md`) — jako čtverec ikony u nadpisu |
| Sekundární tlačítko | `primary-600` plné / 2px obrys | jemné: bílé, 1 px `primary-200`, text `primary-700` (`--soft`) |
| Tlačítka na tmavé ploše | — | `--on-dark` (bílé) a `--on-dark-outline` (1 px bílá 50 %) |
| Formulářové pole | 44 px, rámeček `secondary-200`, prstenec 2 px | 48 px, rámeček `secondary-400`, label nad polem, prstenec 3 px `primary-100` |
| Skladovost | jeden řádek „Skladem 5 258 ks“ | dva řádky: prodejna + součet na 9 prodejnách (`dsk-stk`) |
| Cena v kartě | 24/28, 800 | 22/26, 700 + jednotka „/ ks“ |
| H1 | 44/48, 800 | 40/44, 700 (detail 36/42, mobil 28/34) |
| Nadpis sekce | bez ikony | volitelně ikona ve čtverci 44 px `primary-700` |
| Karusel | šipky v nadpisu | + ghost odkaz; pod 820 px odkaz i šipky v řádku pod karuselem |
| Karta hlavní kategorie | bílá s ikonou | tmavá `primary-900` s fotkou (`dsk-hcard`) |
| Pás výhod | ikony na `primary-50` | bílý pás s čísly a svislými linkami |
| Newsletter | pás `primary-500` | tmavý box `primary-800` na pásu `primary-50` |
| Hlavička | 2 pásy | 3 pásy: utility `primary-900`, hlavní `primary-500`, kategoriová `primary-600` |
| Rozbalovací menu | jen Články | Služby i Články, hover `primary-100` |
| Stav prodejny | plný zelený štítek | zelená tečka + text |

## Nové komponenty

CheckoutSteps, OptionList, CartBar, FormCard (košík), Stock (skladovost), ButtonSurfaces (tlačítka podle podkladu), Notice, Toast, PromoBanner (kampaň, kalkulačka, pomoc), DataTable (Kde řežeme, parametry), Faq, Newsletter. Z dřívějšího seznamu „Chybí“ jsou hotové: košík ve 3 krocích, výběr dopravy a platby, vyhledávání, přihlášení (modal), stavy formulářů (chyba u pole), toast.

## Mapování tříd prototypu

| Stránky | Systém |
| --- | --- |
| `pcard` | `dsk-pcard` |
| `stk`, `stk-my`, `stk-my--no`, `stk-all` | `dsk-stk`, `__my`, `__my--no`, `__all` |
| `carbtn`, `car-all`, `car-nav-m` | `dsk-carbtn`, `dsk-btn--ghost`, `dsk-carnav` |
| `fq-hic`, `ko-bi`, `nz-ic`, `lg-ic` | `dsk-hic` |
| `ko-steps`, `ko-s`, `ko-sn` | `dsk-steps`, `dsk-step`, `dsk-step__n` |
| `ko-o`, `ko-op`, `ko-tip` | `dsk-opt`, `dsk-opt__p`, `dsk-opt__tip` |
| `ko-bar`, `ko-back`, `ko-next` | `dsk-cartbar`, `dsk-btn--on-dark-outline`, `dsk-btn--conversion` + `dsk-btn__two` |
| `ko-note` | `dsk-notice` |
| `kf-card`, `kf-hd`, `kf-in`, `kf-l`, `kf-login` | `dsk-fcard`, `dsk-fcard__hd`, `dsk-input`, `dsk-label`, `dsk-btn--soft` |
| `cb`, `kc`, `nz-help` | `dsk-promo`, `dsk-calc`, `dsk-help` (`--nzu`) |
| `ro-tab`, `ro-yi`, `pd-par` | `dsk-table`, `dsk-yes`, `dsk-params` |
| `fq`, `nl`, `usp` | `dsk-faq`, `dsk-nl`, `dsk-usp` |
| `ct` | `dsk-toast` |
| `hc`, `sv` | `dsk-hcard` |

## Ke sjednocení na stránkách

| Co | Kde | Návrh |
| --- | --- | --- |
| Tlačítka s rádiusem 4 px | Do košíku v kartě, Filtrovat, Vybrat svoji prodejnu, stránkování (čísla, Další, Předchozí), Načíst dalších 24, šipky karuselu, Přihlásit v newsletteru, Odeslat poptávku, Zobrazit 36 produktů a Zrušit filtry ve filtru, Odebrat vše, Hledat ve vyhledávání | 6 px (`radius-md`) |
| Lišta košíku | krok 1 má souhrn pod sebou (popisek nad hodnotou), kroky 2 a 3 v řádku | sjednotit podle kroku 1 (karta CartBar) |
| Hotové kroky košíku | krok 3 (Kontrola) má hotové kroky s tmavým číslem `primary-800`, krok 2 šedé | šedé jako neaktivní (karta CheckoutSteps) |
| Kulaté filtry témat (rádius 999) | blog | čipy s rádiusem 4–6 px |
| Barevné štítky služeb (pastelové) | kontakty | mimo paletu — `dsk-badge--info` nebo `--light` |
| Rychlá poptávka s rámečkem `secondary-400` | blog | `dsk-btn--soft` |
| Registrujte se 46 px | modal přihlášení | 44 px |
| Skladovost v detailu (Jesničánky 12 ks) × přehled po prodejnách (Jesničánky 0 ks) | detail | stejné číslo v obou |
| Podklad upozornění `#FFF6E8` | košík (`ko-note`) | token `main-100` (#FFF4E5) |
| Popisky Porovnat / Přihlásit bíle na `primary-500` | hlavička | 13 px tučně má jen 3,0:1 — zvážit `primary-900` nebo tmavé dlaždice |
| Telefon 26 px v řezu 800 | NZU (`nz-tel`) | 700 podle typografie |

## Stále chybí

| Co | Proč | Priorita |
| --- | --- | --- |
| ProductCard layout B (1000–1149 px) a A (≥ 1150 px, tabulka) | požadavek Master Design Systemu | střední |
| Prázdný košík | stav existuje na webu | střední |
| Rychlý náhled produktu | ikona v kartě | nízká |
| Skeleton načítání karet | Načíst dalších 24 | nízká |
| Barevné logo a SVG | podklady od klienta | — |
