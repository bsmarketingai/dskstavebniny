# CheckoutSteps

Ukazatel 3 kroků objednávky (BSSHOP `OrderNavigator`) nad obsahem všech tří kroků košíku. **Všechny kroky mají stejnou výšku a stejně velké pole s číslem** — liší se jen šířkou a barvou.

| | Desktop (≥ 820 px) | Mobil |
|---|---|---|
| Výška kroku | 64 px | 52 px |
| Pole s číslem | 64 × 64, 700 20 px | 48 × 52, 700 16 px |
| Název | „KROK 1“ 600 12/16 verzálky + název 700 19/24 | jen u aktivního, 700 15/20 |
| Šířka | aktivní 2,2×, ostatní 1× | aktivní zbytek řádku, ostatní jen pole s číslem |
| Mezera | 12 px | 6 px |

Stavy:

- **Aktivní** (`--cur`, `aria-current="step"`): podklad `primary-50`, rámeček `primary-300`, číslo bíle na `primary-700`.
- **Neaktivní** — hotový i budoucí krok vypadají stejně: bílý, rámeček `secondary-200`, číslo `secondary-600` na `secondary-100`, text `secondary-600`.
- **Hotový** (`--done`) je navíc odkaz zpět: hover podklad `primary-50`, číslo na `primary-100`.

Pole s číslem je přilepené k levému okraji a přebírá rádius rodiče (5 0 0 5 uvnitř 6 px).
