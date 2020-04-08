# dungeon-roller
A dungeon roller for Guild Wars 2 that produces a discord-ready event announcement. The event will always be for the next Friday (if today is Friday, it shows the date for today).

Rolls 3 easy, 2 medium, and 1 hard by default though this can be changed using optional arguments.

You can include story dungeons and arah story in the rolls with the `-s` and `-a` optional flags.

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
