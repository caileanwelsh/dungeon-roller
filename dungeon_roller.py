#!/usr/bin/python3
from dungeons import * # class definitions and dungeon variables
import datetime
import argparse
from random import seed
from random import randint

# DEFAULT NUMBER OF PATHS TO ROLL
default_easy_paths = 3
default_medium_paths = 2
default_hard_paths = 1

dungeons = [ac, cm, ta, se, hotw, coe, cof, arah] # list of all dungeons
forbidden_paths = [arah_s] # paths that are excluded from dungeon rolls

# Pick a random dungeon, pick a random path, check its difficulty and if valid add it to paths
# paths is a list of DungeonPaths of the given difficulty
def gen_paths(quantity, difficulty):
    paths = []
    dungeonpaths = []
    while len(paths) < quantity:
        dungeon = dungeons[randint(0, len(dungeons))-1]
        path = dungeon.paths[randint(0, len(dungeon.paths))-1]
        if path not in paths and path not in forbidden_paths and path.difficulty == difficulty:
            paths.append(path)
            dungeonpaths.append(DungeonPath(dungeon, path))
    dungeonpaths.sort(key = lambda x: (x.dungeon.name, x.path.number))
    return dungeonpaths

# Iterate over list of dungeonpaths and print them
def print_dungeonpaths(dungeonpaths):
 for dungeonpath in dungeonpaths:
    print("    {}".format(dungeonpath.str()))

def print_discord_message(easy_paths, medium_paths, hard_paths):
    today = datetime.date.today()
    next_friday = today + datetime.timedelta((4-today.weekday()) % 7)
    print("**— Guild Dungeons {} —**".format(next_friday))
    print("*Gather in the Guild Hall to form groups at 20:00 CET/CEST*")
    print()
    if len(easy_paths) > 0:
        print("Easy dungeon{}:".format("" if len(easy_paths) == 1 else "s"))
        print_dungeonpaths(easy_paths)
        print()
    if len(medium_paths) > 0:
        print("Medium dungeon{}:".format("" if len(medium_paths) == 1 else "s"))
        print_dungeonpaths(medium_paths)
        print()
    if len(hard_paths) > 0:
        print("Hard dungeon{}:".format("" if len(hard_paths) == 1 else "s"))
        print_dungeonpaths(hard_paths)

# Remove story paths or allow arah from rolls
def forbid_paths(forbid_story, allow_arah):
    if forbid_story:
        for dungeon in dungeons:
            for path in dungeon.paths:
                if path.number == 0 and path not in forbidden_paths:
                    forbidden_paths.append(path)
    if allow_arah:
        forbidden_paths.remove(arah_s)

# Count allowed paths by difficulty
def count_paths(dungeons):
    path_totals = {1 : 0, 2: 0, 3:  0}
    for dungeon in dungeons:
        for path in dungeon.paths:
            if path not in forbidden_paths:
                path_totals[path.difficulty]+=1
    return path_totals

def main():
    seed()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--story",
        action="store_false",
        default=True,
        help="include story paths in possible rolls (except arah)")
    parser.add_argument(
        "-a", "--arah",
        action="store_true",
        help="include arah story path in possible rolls")
    parser.add_argument(
        "-e", "--easy",
        type=int,
        default=default_easy_paths,
        help="number of easy paths to roll (default {})".format(default_easy_paths))
    parser.add_argument(
        "-m", "--medium",
        type=int,
        default=default_medium_paths,
        help="number of medium paths to roll (default {})".format(default_medium_paths))
    parser.add_argument(
        "-H", "--hard",
        type=int,
        default=default_hard_paths,
        help="number of hard paths to roll (default {})".format(default_hard_paths))
    args = parser.parse_args()

    forbid_paths(args.story, args.arah)
    path_totals = count_paths(dungeons)

    # Set quantity of paths to max number of paths if quantity exceeds number of available paths
    if args.easy > path_totals[1]:
        args.easy = path_totals[1]
    if args.medium > path_totals[2]:
        args.medium = path_totals[2]
    if args.hard > path_totals[3]:
        args.hard = path_totals[3]

    # ROLL DUNGEONS!!!
    easy_paths = gen_paths(args.easy, 1)
    medium_paths = gen_paths(args.medium, 2)
    hard_paths = gen_paths(args.hard, 3)

    print_discord_message(easy_paths, medium_paths, hard_paths)

if __name__ == "__main__":
    main()
