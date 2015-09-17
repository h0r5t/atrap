from core import LiveTools
from core import HelperTools
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def loadApiKey():
    key_file = open(HelperTools.getApiKeyFile())
    key = key_file.read().strip()
    return key


if __name__ == "__main__":
    LiveTools.showLiveLeagueGames(loadApiKey())
