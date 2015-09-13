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


def loadJsonFromFile(path):
    sample = open(path, encoding="utf8")
    content = sample.read().strip()
    json_obj = json.loads(content)
    return json_obj
