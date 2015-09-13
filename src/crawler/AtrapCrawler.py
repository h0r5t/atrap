from crawler.Dota2ApiWrapper import Dota2ApiWrapper
import HelperTools


class AtrapCrawler:
    def __init__(self):
        api_key = self.loadApiKey()
        self.api_wrapper = Dota2ApiWrapper(api_key)

    def loadApiKey(self):
        key_file = open(HelperTools.getApiKeyFile())
        key = key_file.read().strip()
        return key
