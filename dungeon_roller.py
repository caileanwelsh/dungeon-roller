#!/usr/bin/python3
from random import seed
from random import randint
import datetime

class Dungeon:
    def __init__(self, name, paths):
        self.name = name
        self.paths = paths

class Path:
    def __init__(self, name, number, difficulty):
        self.name = name
        self.number = number
        self.difficulty = difficulty

ac_s = Path("Story",       0, 1)
ac_1 = Path("Hodgins",     1, 1)
ac_2 = Path("Detha",       2, 2)
ac_3 = Path("Tzark",       3, 1)
ac = Dungeon("Ascalonian Catacombs", [ac_s, ac_1, ac_2, ac_3])

cm_s = Path("Story",       0, 1)
cm_1 = Path("Asura",       1, 1)
cm_2 = Path("Seraph",      2, 2)
cm_3 = Path("Butler",      3, 2)
cm = Dungeon("Caudecus Manor", [cm_s, cm_1, cm_2, cm_3])

ta_s = Path("Story",       0, 1)
ta_1 = Path("Leurent",     1, 1)
ta_2 = Path("Vevina",      2, 1)
ta_3 = Path("Aetherpath",  3, 3)
ta = Dungeon("Twilight Arbor", [ta_s, ta_1, ta_2, ta_3])

se_s = Path("Story",       0, 1)
se_1 = Path("Fergg",       1, 1)
se_2 = Path("Rasolov",     2, 2)
se_3 = Path("Koptev",      3, 1)
se = Dungeon("Sorrow's Embrace", [se_s, se_1, se_2, se_3])

hotw_s = Path("Story",     0, 2)
hotw_1 = Path("Butcher",   1, 1)
hotw_2 = Path("Plunderer", 2, 2)
hotw_3 = Path("Zealot",    3, 2)
hotw = Dungeon("Honor of the Waves", [hotw_s, hotw_1, hotw_2, hotw_3])

coe_s = Path("Story",      0, 1)
coe_1 = Path("Submarine",  1, 1)
coe_2 = Path("Teleporter", 2, 2)
coe_3 = Path("Front Door", 3, 1)
coe = Dungeon("Crucibal of Eternity", [coe_s, coe_1, coe_2, coe_3])

cof_s = Path("Story",      0, 1)
cof_1 = Path("Ferrah",     1, 1)
cof_2 = Path("Magg",       2, 1)
cof_3 = Path("Rhiannon",   3, 2)
cof = Dungeon("Citadel of Flame", [cof_s, cof_1, cof_2, cof_3])

arah_s = Path("Story",     0, 3)
arah_1 = Path("Jotun",     1, 3)
arah_2 = Path("Mursaat",   2, 3)
arah_3 = Path("Forgotten", 3, 3)
arah_4 = Path("Seer",      4, 3)
arah = Dungeon("Ruined City of Arah", [arah_s, arah_1, arah_2, arah_3, arah_4])

dungeons = [ac, cm, ta, se, hotw, coe, cof, arah]

def gen_paths(number, difficulty):
    paths = []
    while len(paths) < number:
        dungeon = dungeons[randint(0, len(dungeons))-1]
        path = dungeon.paths[randint(0, len(dungeon.paths))-1]
        if path not in paths and path.difficulty == difficulty:
            paths.append(path)
            print("    {:20s} - Path {:d} ({:s})".format(dungeon.name, path.number, path.name))
    return paths

seed()
today = datetime.date.today()
next_friday = today + datetime.timedelta((4-today.weekday()) % 7)

print("**— Guild Dungeons {} —**".format(next_friday))
print("*Gather in the Guild Hall to form groups at 20:00 CET/CEST*")
print()
print("Easy dungeons:")
easy_paths = gen_paths(3, 1)

print()
print("Medium dungeons:")
med_paths = gen_paths(2, 2)

print()
print("Bonus hard dungeon:")
hard_paths = gen_paths(1, 3)
