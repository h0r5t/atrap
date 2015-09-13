import os


def getParentDir(dir):
    return os.path.abspath(os.path.join(dir, '..'))


def getApiKeyFile():
    return getParentDir(getParentDir(getParentDir(__file__))) + '\\api_key.key'
