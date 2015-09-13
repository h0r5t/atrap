import urllib2
import json


class Dota2ApiWrapper():

    def __init__(self, api_key):

        self.GET_LEAGUE_LISTING = "https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v0001/"
        self.GET_LIVE_LEAGUE_GAMES = "https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v0001/"

        self.api_key = api_key
        self.key_string = "?key=" + api_key

    def getLeagueListing(self):
        url = self.GET_LEAGUE_LISTING + self.key_string
        return self.getJsonObjectForApiCall(url)

    def getLiveLeagueGames(self):
        url = self.GET_LIVE_LEAGUE_GAMES + self.key_string
        return self.getJsonObjectForApiCall(url)

    def getJsonObjectForApiCall(self, url):
        json_response = urllib2.urlopen(url).read()
        json_object = json.loads(json_response)
        return json_object
