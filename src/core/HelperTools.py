import os
import json


def getParentDir(dir):
    return os.path.abspath(os.path.join(dir, '..'))


def getApiKeyFile():
    return getParentDir(getParentDir(getParentDir(__file__))) + '\\config\\api_key.key'


def getConfigFile():
    return getParentDir(getParentDir(getParentDir(__file__))) + '\\config\\config.cfg'


def getTeamsFile():
    return getParentDir(getParentDir(getParentDir(__file__))) + '\\static\\teams\\teams.json'


def loadJsonFromFile(path):
    sample = open(path, encoding="utf8")
    content = sample.read().strip()
    json_obj = json.loads(content)
    return json_obj
