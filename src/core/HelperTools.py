import os
import json


def getParentDir(dira):
    return os.path.abspath(os.path.join(dira, '..'))


def getApiKeyFile():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "config", "api_key.key")


def getConfigFile():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "config", "config.cfg")


def getTeamsFile():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "static", "teams", "teams.json")


def getPlayersDir():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "static", "players")


def getWebDir():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "web")


def getPlayerPositionsFile():
    return os.path.join(getPlayersDir(), "player_positions.json")


def loadJsonFromFile(path):
    if not os.path.isfile(path):
        return {}
    sample = open(path, encoding="utf8")
    content = sample.read().strip()
    if (content == ""):
        return {}
    json_obj = json.loads(content)
    return json_obj


def saveJsonToFile(json_obj, path):
    json.dump(json_obj, path, sort_keys=True, indent=4, separators=(',', ': '))
