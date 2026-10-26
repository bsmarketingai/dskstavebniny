# ProductCard

Karta produktu ve výpisu i karuselu — layout **C (stacked)**, platí pod 1000 px i v mřížkách na desktopu. Pořadí: obrázek se štítky → název (max. 2 řádky) → krátký popis (od 550 px) → skladovost → cena s DPH a bez DPH → číselník + Do košíku. Celá karta nemá stín; `secondary-200` rámeček, `radius-md`.

Layouty **B (compact block, 1000–1149 px)** a **A (full table, ≥1150 px)** z Master Design Systemu zatím nejsou navržené.

**Hover:** karta se zvedne o 6 px a dostane měkký stín (300 ms ease tam i zpět) a název se podtrhne; rámeček se nemění. S `prefers-reduced-motion` bez pohybu. Karusel má nahoře 8 px rezervu, aby se zvednutá karta neořízla. Jinak karty stín nemají.