# dungeon-roller
A dungeon roller for Guild Wars 2 that produces a discord-ready event announcement. The event will always be for the next Friday (if today is Friday, it shows the date for today).

Rolls 3 easy, 2 medium, and 1 hard by default though this can be changed using optional arguments.

You can include story dungeons and Arah story in the rolls with the `-s` and `-a` optional flags.

Dungeon difficulty is assessed on the assumption that at least one knowledgeable person will be in the dungeon group.

```
usage: dungeon_roller.py [-h] [-s] [-a] [-e EASY] [-m MEDIUM] [-H HARD]

optional arguments:
  -h, --help            show this help message and exit
  -s, --story           include story paths (except arah)
  -a, --arah            include arah story path
  -e EASY, --easy EASY  number of easy paths to roll (default 3)
  -m MEDIUM, --medium MEDIUM
                        number of medium paths to roll (default 2)
  -H HARD, --hard HARD  number of hard paths to roll (default 1)
```

Easy dungeons:
    Ascalonian Catacombs - Path 0 (Story)
    Ascalonian Catacombs - Path 1 (Hodgins)
    Ascalonian Catacombs - Path 3 (Tzark)
    Caudecus Manor       - Path 0 (Story)
    Caudecus Manor       - Path 1 (Asura)
    Citadel of Flame     - Path 0 (Story)
    Citadel of Flame     - Path 1 (Ferrah)
    Citadel of Flame     - Path 2 (Magg)
    Crucibal of Eternity - Path 0 (Story)
    Crucibal of Eternity - Path 1 (Submarine)
    Crucibal of Eternity - Path 3 (Front Door)
    Honor of the Waves   - Path 1 (Butcher)
    Sorrow's Embrace     - Path 0 (Story)
    Sorrow's Embrace     - Path 1 (Fergg)
    Sorrow's Embrace     - Path 3 (Koptev)
    Twilight Arbor       - Path 0 (Story)
    Twilight Arbor       - Path 1 (Leurent)
    Twilight Arbor       - Path 2 (Vevina)

Medium dungeons:
    Ascalonian Catacombs - Path 2 (Detha)
    Caudecus Manor       - Path 2 (Seraph)
    Caudecus Manor       - Path 3 (Butler)
    Citadel of Flame     - Path 3 (Rhiannon)
    Crucibal of Eternity - Path 2 (Teleporter)
    Honor of the Waves   - Path 0 (Story)
    Honor of the Waves   - Path 2 (Plunderer)
    Honor of the Waves   - Path 3 (Zealot)
    Sorrow's Embrace     - Path 2 (Rasolov)

Hard dungeons:
    Ruined City of Arah  - Path 0 (Story)
    Ruined City of Arah  - Path 1 (Jotun)
    Ruined City of Arah  - Path 2 (Mursaat)
    Ruined City of Arah  - Path 3 (Forgotten)
    Ruined City of Arah  - Path 4 (Seer)
    Twilight Arbor       - Path 3 (Aetherpath)

