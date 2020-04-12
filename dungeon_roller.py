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

easy_description = "Easy"
medium_description = "Medium"
hard_description = "Hard"

donegeons = [] # list of dungeons that have already been printed, used for deciding if to print waypoint link

def find_available_paths(allow_story, allow_arah, dungeons):
    available_dungeonpaths = [[], [], []]
    for dungeon in dungeons:
        for path in dungeon.paths:
            if not allow_story and path.number == 0:
                continue
            if not allow_arah and path == arah_s:
                continue
            available_dungeonpaths[path.difficulty].append(DungeonPath(dungeon, path))
    return available_dungeonpaths

def roll_dungeonpaths(desired_quantity, available_dungeonpaths):
    rolled_dungeonpaths = []
    while len(rolled_dungeonpaths) <= desired_quantity:
        i = randint(0, len(available_dungeonpaths)-1)
        rolled_dungeonpaths.append(available_dungeonpaths.pop(i))

    # Return list of dungeonpaths sorted alphabetically by dungeon name and then in ascending order of path number
    return sorted(rolled_dungeonpaths, key = lambda dungeonpath: (dungeonpath.dungeon.name, dungeonpath.path.number))

def print_dungeonpaths(dungeonpaths, description):
    if len(dungeonpaths) > 0:
        print("{} dungeon{}:".format(description, "" if len(dungeonpaths) == 1 else "s"))

        for dungeonpath in dungeonpaths:
            print((" " * 3),"{}".format(dungeonpath.str()), end="") # remove newline from print()
            # print the waypoint code if it hasn't already been printed
            if dungeonpath.dungeon not in donegeons:
                print("\t", dungeonpath.dungeon.waypoint)
            else:
                print()
            donegeons.append(dungeonpath.dungeon)
        print()

def print_discord_message(easy_paths, medium_paths, hard_paths, date, time):
    print("**— Guild Dungeons {} —**".format(date))
    print("*Gather in the Guild Hall to form groups at {}*".format(time))
    print()
    print_dungeonpaths(easy_paths, easy_description)
    print_dungeonpaths(medium_paths, medium_description)
    print_dungeonpaths(hard_paths, hard_description)

def list_all_dungeonpaths(dungeonpathslist):
    print_dungeonpaths(dungeonpathslist[0], easy_description)
    print_dungeonpaths(dungeonpathslist[1], medium_description)
    print_dungeonpaths(dungeonpathslist[2], hard_description)

def roll_dungeons(easy, medium, hard, available_dungeonpathslist):

    # Set quantity of paths to max number of paths if quantity exceeds number of available paths
    if easy > len(available_dungeonpathslist[0])-1:
        easy = len(available_dungeonpathslist[0])-1
    if medium > len(available_dungeonpathslist[1])-1:
        medium = len(available_dungeonpathslist[1])-1
    if hard > len(available_dungeonpathslist[2])-1:
        hard = len(available_dungeonpathslist[2])-1

    # ROLL DUNGEONS!!!
    easy_paths = roll_dungeonpaths(easy, available_dungeonpathslist[0])
    medium_paths = roll_dungeonpaths(medium, available_dungeonpathslist[1])
    hard_paths = roll_dungeonpaths(hard, available_dungeonpathslist[2])

    today = datetime.date.today()
    # next friday is today if today is friday
    next_friday = today + datetime.timedelta((4-today.weekday()) % 7)

    print_discord_message(easy_paths, medium_paths, hard_paths, next_friday, "20:00 CET/CEST")

def main():
    seed()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--story",
        action="store_true",
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
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="list all available dungeon paths")
    args = parser.parse_args()

    dungeons = [ac, cm, ta, se, hotw, coe, cof, arah] # list of all dungeons

    if args.list:
        available_dungeonpaths = find_available_paths(True, True, dungeons)
        list_all_dungeonpaths(available_dungeonpaths)
    else:
        available_dungeonpaths = find_available_paths(args.story, args.arah, dungeons)
        roll_dungeons(args.easy, args.medium, args.hard, available_dungeonpaths)

if __name__ == "__main__":
    main()
