# CartBar

Plovoucí lišta na spodku všech tří kroků košíku (BSSHOP `OrderActionPanelHorizontal`) — tmavý pás `primary-800` přes celou šířku se stínem `shadow-bar`, poslední prvek stránky (v košíku není FAQ, newsletter ani patička). Layout podle kroku 1 košíku:

**Desktop (≥ 820 px)** — jeden řádek, výška 88 px, padding 12 × okraj stránky:

1. vlevo **Zpět** (`--on-dark-outline --xl`, 64 px, rámeček bílá 45 %): „Zpět k nákupu“ / „Zpět do košíku“ / „Zpět ke kontaktním údajům“;
2. vpravo u tlačítka **souhrn** — dvě položky vedle sebe (mezera 32), v každé popisek nahoře (500 15/20 `primary-200`) a hodnota pod ním (mezera 10): Poštovné a balné **0 Kč** (700 17/22), Konečná cena s DPH **7 857,80 Kč** (700 32/36, zarovnaná doprava);
3. **Pokračovat** (`--conversion --xl`, 64 px) s dvouřádkovým popiskem: Pokračovat / ke kontaktním údajům → ke kontrole údajů → Odeslat objednávku / s povinností platby.

**Mobil** — dva řádky, padding 8 16: nahoře souhrn přes celou šířku (poštovné vlevo 12/16 + 14/18, konečná cena vpravo 12/16 + 22/26); dole Zpět jen jako ikona 48 × 48 vlevo a Pokračovat 48 px vpravo (popisek 16/20 + 12/15).
