# dungeon-roller
A dungeon roller for Guild Wars 2 that produces a discord-ready event announcement. Rolls 3 easy, 2 medium, and 1 hard dungeon by default though this can be changed using optional arguments.

Dungeon difficulty is assessed on the assumption that at least one knowledgeable person will be in the dungeon group.

```
usage: dungeon_roller.py [-h] [-e {0..18}] [-m {0..9}] [-H {0..5}]

optional arguments:
  -h, --help            show this help message and exit
  -e {0..18}, --easy {0..18}
                        number of easy paths to roll (default 3)
  -m {0..9}, --medium {0..9}
                        number of medium paths to roll (default 2)
  -H {0..5}, --hard {0..5}
                        number of hard paths to roll (default 1)
```
