# PriceStock

**Cena:** s DPH vždy hlavní (`primary-700`, v kartě 22/26, v detailu `--lg` 40/44), za ní jednotka „/ ks“ (`dsk-price__unit`), přeškrtnutá původní cena vpravo červeně, pod tím cena bez DPH (`caption`, `secondary-600`). Červená je vyhrazená slevám, cena sama červená není.

**Skladovost — jedna komponenta všude** (karta, výpis, karusel, detail, mini košík, popup, našeptávač, košík): `dsk-stk` = dva řádky. Nahoře vybraná prodejna: zelený check + „Jesničánky: **48 ks**“ (`success`); když tam není, hodiny + „Jesničánky: 0 ks“ v `main-700`. Pod tím „Celkem na 9 prodejnách: **5 258 ks**“ (`secondary-600`, odsazeno pod text). Na stránkách odpovídá třídám `.stk / .stk-my / .stk-my--no / .stk-all`. Jiné zápisy skladovosti („Skladem 5 258 ks“, „Na objednávku“) nepoužíváme.
