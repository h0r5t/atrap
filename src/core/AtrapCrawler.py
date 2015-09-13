from core.Dota2ApiWrapper import Dota2ApiWrapper
import HelperTools
import time


class AtrapCrawler():
    def __init__(self):
        self.configMap = self.loadConfig()
        api_key = self.loadApiKey()
        self.api_wrapper = Dota2ApiWrapper(api_key)
        self.relevantActiveGames = []

    def start(self):
        while(True):

            relevantLiveGames = self.getRelevantLiveLeagueGames()

            time.sleep(int(self.configMap["crawler_sleep_time"]))

    def getRelevantLiveLeagueGames(self, list_of_team_ids):
        passads

    def loadConfig(self):
        configMap = {}
        config_file = open(HelperTools.getConfigFile())
        for line in config_file:
            key = line.split(':')[0].strip()
            value = line.split(':')[1].strip()
            configMap[str(key)] = str(value)
        return configMap

    def loadApiKey(self):
        key_file = open(HelperTools.getApiKeyFile())
        key = key_file.read().strip()
        return key

if __name__ == '__main__':
    crawler = AtrapCrawler()
    crawler.start()
