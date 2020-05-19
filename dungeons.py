class Dungeon:
    def __init__(self, name, paths, waypoint):
        self.name = name
        self.paths = paths # list of paths
        self.waypoint = waypoint

class Path:
    def __init__(self, name, number, difficulty, level):
        self.name = name
        self.number = number
        self.difficulty = difficulty # 0-2, 0 is easy, 2 is hard
        self.level = level # minimum character level expected for dungeon path, was used for sorting but not any more

class DungeonPath:
    def __init__(self, dungeon, path):
        self.dungeon = dungeon
        self.path = path

    # Nicely formatted string of a dungeon path
    def str(self):
        return "{:20s} - Path {:d} ({:s})".format(self.dungeon.name, self.path.number, self.path.name)

    def str_wpt(self):
        return "{:42s} {}".format(DungeonPath.str(self), self.dungeon.waypoint)

ac_s = Path("Story",       0, 0, 20)
ac_1 = Path("Hodgins",     1, 0, 25)
ac_2 = Path("Detha",       2, 1, 25)
ac_3 = Path("Tzark",       3, 0, 25)
ac = Dungeon("Ascalonian Catacombs", [ac_s, ac_1, ac_2, ac_3], "[&BIYBAAA=]")

cm_s = Path("Story",       0, 0, 40)
cm_1 = Path("Asura",       1, 0, 45)
cm_2 = Path("Seraph",      2, 1, 45)
cm_3 = Path("Butler",      3, 1, 45)
cm = Dungeon("Caudecus Manor", [cm_s, cm_1, cm_2, cm_3], "[&BPoAAAA=]")

ta_s = Path("Story",       0, 0, 50)
ta_1 = Path("Up",     1, 0, 55)
ta_2 = Path("Forward",      2, 0, 55)
ta_3 = Path("Aetherpath",  3, 2, 55)
ta = Dungeon("Twilight Arbor", [ta_s, ta_1, ta_2, ta_3], "[&BEEFAAA=]")

se_s = Path("Story",       0, 0, 60)
se_1 = Path("Fergg",       1, 0, 65)
se_2 = Path("Rasolov",     2, 1, 65)
se_3 = Path("Koptev",      3, 0, 65)
se = Dungeon("Sorrow's Embrace", [se_s, se_1, se_2, se_3], "[&BFYCAAA=]")

cof_s = Path("Story",      0, 0, 70)
cof_1 = Path("Ferrah",     1, 0, 75)
cof_2 = Path("Magg",       2, 0, 75)
cof_3 = Path("Rhiannon",   3, 1, 75)
cof = Dungeon("Citadel of Flame", [cof_s, cof_1, cof_2, cof_3], "[&BEAFAAA=]")

hotw_s = Path("Story",     0, 1, 76)
hotw_1 = Path("Butcher",   1, 0, 80)
hotw_2 = Path("Plunderer", 2, 1, 80)
hotw_3 = Path("Zealot",    3, 1, 80)
hotw = Dungeon("Honor of the Waves", [hotw_s, hotw_1, hotw_2, hotw_3], "[&BEMFAAA=]")

coe_s = Path("Story",      0, 0, 78)
coe_1 = Path("Submarine",  1, 0, 80)
coe_2 = Path("Teleporter", 2, 1, 80)
coe_3 = Path("Front Door", 3, 0, 80)
coe = Dungeon("Crucibal of Eternity", [coe_s, coe_1, coe_2, coe_3], "[&BEIFAAA=]")

arah_s = Path("Story",     0, 2, 80)
arah_1 = Path("Jotun",     1, 2, 80)
arah_2 = Path("Mursaat",   2, 2, 80)
arah_3 = Path("Forgotten", 3, 2, 80)
arah_4 = Path("Seer",      4, 2, 80)
arah = Dungeon("Ruined City of Arah", [arah_s, arah_1, arah_2, arah_3, arah_4], "[&BCADAAA=]")
