from __future__ import print_function
from urllib.request import urlopen
import json
import codecs
from core.ApiObjects import LiveLeagueGamesList
from core.ApiObjects import MatchDetails


class Dota2ApiWrapper():

    def __init__(self, api_key):

        self.GET_LEAGUE_LISTING = "https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v0001/"
        self.GET_LIVE_LEAGUE_GAMES = "https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v0001/"
        self.GET_MATCH_DETAILS = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/"

        self.api_key = api_key
        self.key_string = "?key=" + api_key

    def getLeagueListing(self):
        url = self.GET_LEAGUE_LISTING + self.key_string
        return self.getJsonObjectForApiCall(url)

    def getLiveLeagueGames(self):
        url = self.GET_LIVE_LEAGUE_GAMES + self.key_string
        obj = self.getJsonObjectForApiCall(url)
        if len(obj) == 0:
            return None
        return LiveLeagueGamesList(obj).getGames()

    def getMatchDetails(self, match_id):
        url = self.GET_MATCH_DETAILS + self.key_string + "&match_id=" + str(match_id)
        obj = self.getJsonObjectForApiCall(url)
        if len(obj) == 0:
            return None
        return MatchDetails(obj)

    def getJsonObjectForApiCall(self, url):
        try:
            json_response = urlopen(url)
            reader = codecs.getreader("utf-8")
            json_object = json.load(reader(json_response))
        except:
            # Test.warning("error loading json from url: " + str(url))
            return {}

        return json_object
