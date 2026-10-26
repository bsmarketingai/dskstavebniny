# DSK Stavebniny – struktura e-shopové části (dskstavebniny.cz)

Podklad pro redesign v Claude Design. Zmapováno procházením živého webu 14. 9. 2026. Platforma: BSSHOP (e-shop napojený na Pohodu).

## 1. Hlavička (globální, na všech stránkách e-shopu)

- **Logo** DSK stavebniny (odkaz na Úvod)
- **Hlavní navigace:** Úvod / E-shop / Služby / Články / Novinky a akce / Průmyslová práva / Kariéra / Kontakty
- **Utility panel se 6 kontaktními zkratkami** (každá s telefonním číslem): Rychlá poptávka (+ formulář), Objednávky z e-shopu, Technické dotazy, Pomoc s dotacemi, Kontakt – ukrajinsky, Hledáte práci?
- **Přihlášení / Registrujte se** (rozbalovací mini-formulář přímo v hlavičce – e-mail + heslo)
- **Ikona hledání** – otevírá modal s jedním polem a tlačítkem Hledat
- **Widget košíku** – počet produktů + celková cena, odkaz „vstoupit do košíku"

## 2. Vstupní stránka e-shopu (/eshop/)

Dlaždicová mřížka hlavních kategorií (3× obrázek + název + krátký popis náplně):

1. Stavebniny – betonové výrobky, cihly, fasády, izolace, hutní materiál, suchá stavba, lepenky, řezivo, fólie
2. Cenově výhodné produkty *(kurátorská kolekce napříč kategoriemi, ne skutečná kategorie)*
3. Kotvení a spojování – vruty, šrouby, hmoždinky, hřebíky, podložky a matky, tesařské kování
4. Nářadí – ruční, elektrické a AKU nářadí a příslušenství, stavební a zahradní technika
5. Stavební chemie – tmely, silikony, pěny, lepidla, penetrace, ředidla, přísady do stavebních hmot
6. Barvy a nátěry – fasádní a interiérové barvy, nátěry na dřevo, kov i beton, spreje
7. Bydlení a zahrada – bazénové příslušenství, osivo a substráty, hnojiva a postřiky, brikety
8. Pracovní oděvy a obuv – ochranné pracovní pomůcky, pracovní i trekingová obuv, oblečení
9. Poukazy – dárkové poukazy v 6 nominálních hodnotách
10. Výprodej – fullwidth banner pod dlaždicemi, samostatná kategorie se zlevněným zbožím

**Zjištěná nesrovnalost:** postranní menu „Kategorie e-shopu" (viz bod 3) obsahuje navíc kategorie **Termalica – zdicí prvky** a **Auto-moto**, které na vstupní dlaždicové stránce chybí. Při redesignu stojí za sjednocení.

## 3. Postranní menu „Kategorie e-shopu" (perzistentní na všech listovacích stránkách)

Nad výpisem hlavních kategorií jsou samostatné odkazy na **akční/kurátorské výběry**:
- Akce (aktuální kampaně – např. „Ztracené bednění až o 25 % výhodněji", „Prázdniny s UNiG kombi Elegant", „Šedý EPS za cenu bílého")
- Cenově výhodné produkty
- Unikátní produkty
- Top produkty

Pod tím plný strom **10 hlavních kategorií**: Stavebniny · Barvy a nátěry · Stavební chemie · Nářadí · Kotvení a spojování · Termalica – zdicí prvky · Bydlení a zahrada · Pracovní oděvy a obuv · Auto-moto · Výprodej.

Po rozkliknutí kategorie se menu rozbaluje **stromově in-line** (odsazované „»" úrovně) – aktuální větev zůstává vizuálně otevřená, uživatel vidí celou cestu i sourozenecké položky.

## 4. Hloubka kategorizace (na příkladu Stavebniny)

Kategorie jsou vnořené až do **4–5 úrovní**, poslední úroveň bývá filtr podle výrobce/značky:

```
Stavebniny
└─ Zdící materiály
   └─ Keramické zdivo
      └─ Broušené keramické zdivo
         └─ Klasické zdivo
            └─ Obvod
               └─ [výrobce] Heluz / KM Beta / Leier / MziegeL / Porotherm / Winklmann / Ostatní výrobci
            └─ Příčky / Soklové zdivo / Věncovky
         └─ Akustické zdivo / Izolační zdivo
      └─ Nebroušené keramické zdivo / Překlady / Stropy
   └─ Pórobetonové zdivo / Cihly / Ztracené bednění / Betonové zdivo / Bednění věnců /
      Vápenopískové zdivo / Příslušenství, přípravky, kotvy / Luxfery
└─ Betonové výrobky · Fasády, maltové směsi · Tepelné izolace · Lepenky, hydroizolace ·
   Hutní materiály · Suchá stavba · Stavební fólie · Střechy · Stavební řezivo ·
   Příslušenství fasád · Kamenné koberce · Písky, štěrky, kamenivo · Cement, vápno, sádra ·
   Keramické obklady, dlažby a sanita · Dveře, zárubně, zámky a kování · Okna ·
   Drátěné ploty · Komíny, krbová kamna, topidla · Vnitřní a vnější rozvody ·
   Podlahové krytiny · (a další – výpis není vyčerpávající, kategorie Stavebniny má 20+ větví)
```

Každá úroveň je zároveň **plnohodnotná listovací stránka** – nejde jen o „prázdný" rozcestník, ale o hybrid rozcestník + filtrovaný výpis produktů (viz bod 5).

## 5. Šablona: kategorie / výpis produktů

Společné pro všechny úrovně kategorií:

1. **Breadcrumb** (celá cesta stromem, klikací)
2. **Nadpis + volitelný úvodní text** (u některých kategorií edukativní odstavec, např. rozdíl broušená/nebroušená cihla)
3. **Dlaždice podkategorií** (obrázek + název), pokud existují potomci
4. **Filtrovací panel:**
   - checkbox „Skladem"
   - cenový rozsah (slider + dvě číselná pole)
   - rychlé příznaky: Akce / Novinky / Výprodej
   - **parametrické filtry specifické pro kategorii** (rozbalovací akordeon), např. u zdiva: Pevnost v tlaku [MPa], Délka/Šířka/Výška [mm], Hmotnost [kg], Kusů na paletě, Tepelný odpor [R], Součinitel prostupu tepla [U], Spotřeba [ks/m²], Spotřeba [ks/m³], Výrobce
   - fulltextové hledání „v této kategorii" se scope volbami (v kódech / v názvu / v popisu)
5. **Ovládání výpisu:** řazení (Řadit dle: Výchozí…), počet na stránku (Zobrazit: 60…), počet nalezených produktů, stránkování
6. **Grid produktových karet** – viz bod 6

## 6. Produktová karta (v gridu)

- Fotka produktu
- Název (často vč. rozměrů/kódu výrobku v názvu)
- Dostupnost skladem (počet ks, zeleně)
- Ikona rychlého náhledu (lupa)
- Krátký popis (2–3 řádky)
- Cena s DPH (výrazně, červeně) + cena bez DPH (drobně)
- Volitelný badge: „Věrnostní program", „Cenově výhodný produkt" apod.
- Číselník množství + tlačítko „přidat do košíku" (ikona košíku)

## 7. Detail produktu

1. Breadcrumb (plná cesta stromem vč. větve výrobce)
2. Název produktu
3. Obrázek (s možností zoomu/watermarku)
4. Cena s DPH (velká, červená) + cena bez DPH
5. Dostupnost + tlačítko Koupit s číselníkem množství
6. **Tabulka skladové dostupnosti po jednotlivých pobočkách** (9 poboček: Opatovice nad Labem, Hradec Králové, Holice, Mnichovo Hradiště, Týnec nad Labem, Pardubice-Jesničánky, Pardubice-Černá za Bory, Nové Město nad Metují, Týniště nad Orlicí) + poznámka o aktualizaci 1×/60 min
7. Akční odkazy: Hlídací pes (hlídání dostupnosti/ceny), Porovnat, Přidat k oblíbeným, Význam štítků, Dotaz na prodejce
8. Metadata: Kód produktu, Výrobce, Záruka
9. Karusel „Související produkty"
10. Taby: **Popis** / **Parametry** / **Podrobnosti**
11. Sekce „Alternativní produkty"

## 8. Vyhledávání (/hledat/)

- Vstupní pole + scope checkboxy (v kódech / v názvu / v popisu)
- Sekce „Nalezené stránky" (obsahové/redakční výsledky – odděleně od produktů)
- Pod tím identický produktový grid + filtrační panel jako u kategorie (bod 5), ale napříč celým katalogem

## 9. Košík a objednávkový proces

Třístupňový wizard s indikátorem kroků nahoře:

1. **Nákupní košík** – tabulka položek (název, dostupnost, množství, cena/ks, cena celkem, smazání), výběr **způsobu dopravy** (osobní odběr na některé z 9 poboček, nebo „Doprava na stavbu" s dopočítanou cenou) a **způsobu platby** (hotově na prodejně, kartou na prodejně, převodem/příkazem předem)
2. **Kontaktní údaje**
3. **Kontrola údajů**

Prázdný košík má vlastní ilustrovaný stav („Košík je prázdný…" + tlačítko Zpět do obchodu).

## 10. Patička (globální)

- **Adresa firmy** – sídlo, IČO/DIČ, zápis v OR
- **DSK – obchod** – Obchodní podmínky, Možnosti platby, Způsoby doručení, Reklamační řád, Reklamační formulář, Ochrana osobních údajů, Řešení mimosoudních sporů
- **Ostatní** – Aktuality, Kariéra, Věrnostní program, Naši dodavatelé, Naši dlužníci, Podpora v ukrajinštině
- **Odběr novinek** – e-mail + GDPR souhlas + tlačítko Přihlásit
- **Podporujeme** – CSR banner (450 ml NADĚJE)
- Spodní lišta: copyright, „Návrh a správa webu", „BSSHOP: e-shop napojený na Pohodu", odkaz „Zobrazit mobilní verzi"

---

## Poznámky k redesignu

- **Filtrovací panel je nejsilnější, ale vizuálně nejzastaralejší prvek** – akordeon s parametry (Pevnost v tlaku, Délka…) má velký potenciál pro modernější UI (chipy, aktivní filtry nahoře, sticky panel).
- **Hloubka 4–5 úrovní kategorií** bude klíčové UX téma – zvážit mega menu / drobečkovou navigaci s vizuální hierarchií, aby se uživatel neztrácel.
- **Produktová karta** míchá hodně informací (cena s/bez DPH, sklad, popis, badge, quantity picker) – prostor pro vizuální prioritizaci.
- Nesrovnalost hlavních kategorií mezi vstupní stránkou e-shopu a postranním menu (Termalica, Auto-moto) – dobrý bod pro sjednocení IA při redesignu.
- Tabulka skladové dostupnosti po pobočkách na detailu produktu je unikátní a hodnotný prvek (9 poboček, 3 kraje) – v novém designu stojí za zvýraznění, ne skrytí.
- Výpis kategorie Stavebniny obsahuje 20+ podkategorií – pro kompletní vyčerpávající strom by bylo efektivnější exportovat kategorie přímo z administrace/sitemapy než dál procházet ručně.

---

## Rozhodnutí v redesignu (stav návrhu)

- **Výběry nad stromem:** Akce, Cenově výhodné produkty, Unikátní produkty a Top produkty jsou samostatná skupina nad stromem kategorií (sidebar i megamenu). Cenově výhodné produkty jsou kolekce, ne kategorie, proto ve stromu nejsou.
- **Strom kategorií e-shopu:** Stavebniny, Barvy a nátěry, Stavební chemie, Nářadí, Kotvení a spojování, Bydlení a zahrada, Pracovní oděvy a obuv, Poukazy, Výprodej. **Termalica – zdicí prvky a Auto-moto zatím chybí — čeká na rozhodnutí, zda je do sjednoceného stromu přidat, nebo zrušit.**
- **Stavebniny, 1. úroveň (21 větví):** Zdící materiály, Betonové výrobky, Fasády a maltové směsi, Tepelné izolace, Lepenky a hydroizolace, Hutní materiály, Suchá stavba, Stavební fólie, Střechy, Stavební řezivo, Příslušenství fasád, Kamenné koberce, Písky, štěrky a kamenivo, Cement, vápno a sádra, Keramické obklady, dlažby a sanita, Dveře, zárubně, zámky a kování, Okna, Drátěné ploty, Komíny, krbová kamna a topidla, Vnitřní a vnější rozvody, Podlahové krytiny.
- **Megamenu** je kaskáda: kategorie → podkategorie → potomci s fotkami. Sidebar je stromový in-line, aktivní větev zůstává otevřená.
- **Cena v kartě** je v `primary-700`, ne červeně jako na současném webu: červená je vyhrazená pro výprodej a slevu, aby sleva byla poznat.
- **Detail:** taby Popis / Parametry / Podrobnosti; tabulka skladovosti 9 poboček s poznámkou o aktualizaci 1× za 60 min; akce Dotaz na prodejce, Hlídací pes, Porovnat, Oblíbené, Význam štítků, Tisk.
