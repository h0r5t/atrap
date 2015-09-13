from urllib.request import urlopen
import json
import codecs
from core.ApiObjects import LiveLeagueGamesList


class Dota2ApiWrapper():

    def __init__(self, api_key):

        self.GET_LEAGUE_LISTING = "https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v0001/"
        self.GET_LIVE_LEAGUE_GAMES = "https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v0001/"

        self.api_key = api_key
        self.key_string = "?key=" + api_key

    def test(self):
        return "test1"

    def getLeagueListing(self):
        url = self.GET_LEAGUE_LISTING + self.key_string
        return self.getJsonObjectForApiCall(url)

    def getLiveLeagueGames(self):
        url = self.GET_LIVE_LEAGUE_GAMES + self.key_string
        return LiveLeagueGamesList(self.getJsonObjectForApiCall(url)).getGames()

    def getJsonObjectForApiCall(self, url):
        try:
            json_response = urlopen(url)
            reader = codecs.getreader("utf-8")
            json_object = json.load(reader(json_response))
        except:
            return {}

        return json_object
