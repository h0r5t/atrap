import os
import json


def getParentDir(dira):
    return os.path.abspath(os.path.join(dira, '..'))


def getApiKeyFile():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "config", "api_key.key")


def getLogFile():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "web", "live", "log.txt")


def getConfigFile():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "config", "config.cfg")


def getTeamsFile():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "static", "teams", "teams.json")


def getTestResourcesDir():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "test", "res")


def getPlayersDir():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "web", "live", "players")


def getMatchesDir():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "web", "live", "matches")


def getMatchFile(match_id):
    return os.path.join(getMatchesDir(), str(match_id) + ".json")


def getWebDir():
    return os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "web")


def getPlayerPositionsFile():
    return os.path.join(getPlayersDir(), "player_positions.json")


def log(string):
    with open(getLogFile(), 'a') as f:
        f.write(str(string) + '\n')


def loadJsonFromFile(path):
    if not os.path.isfile(path):
        return {}
    sample = open(path, encoding="utf8")
    content = sample.read().strip()
    if (content == ""):
        return {}
    json_obj = json.loads(content)
    return json_obj
