from crawler.Dota2ApiWrapper import Dota2ApiWrapper


class AtrapCrawler:
    def __init__(self):
        api_key = self.loadApiKey()
        api_wrapper = Dota2ApiWrapper(api_key)

    def loadApiKey(self):
        print("hi")
