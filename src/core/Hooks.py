import os
from core import HelperTools
import json


class Hook():

    def __init__(self):
        pass

    def update(self):
        raise NotImplementedError("This is an abstract class")


class PlayerListHook(Hook):

    def __init__(self):
        pass

    def update(self):
        players_dir = HelperTools.getPlayersDir()
        player_file = os.path.join(HelperTools.getWebDir(), "live", "player_list.json")

        json_obj = {}

        player_ids = []
        for f in os.listdir(players_dir):
            player_ids.append(int(f.split(".")[0]))

        json_obj["all_players"] = player_ids

        saveJsonToFile(json_obj, player_file)


def saveJsonToFile(json_obj, path):
    with open(path, "w") as f:
        f.truncate()
        json.dump(json_obj, f, sort_keys=True, indent=4, separators=(',', ': '))
