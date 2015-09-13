from core.Dota2ApiWrapper import Dota2ApiWrapper
from core import HelperTools
import time


class AtrapCrawler():
    def __init__(self):
        self.configMap = self.loadConfig()
        api_key = self.loadApiKey()
        self.api_wrapper = Dota2ApiWrapper(api_key)
        self.allRelevantGames = []
        self.finishedGames = []

    def start(self):
        while(True):

            teamsList = self.loadTeams()
            team_id_list = self.genereateTeamIDList(teamsList)

            relevantLiveGames = self.getRelevantLiveLeagueGames(team_id_list)
            # iterate over games, parse finished games and make relevantgames
            # the list

            time.sleep(int(self.configMap["crawler_sleep_time"]))

    def getRelevantLiveLeagueGames(self, list_of_team_ids):
        # IDs need to be in string format
        relevantGames = []
        liveGames = self.api_wrapper.getLiveLeagueGames()

        for game in liveGames:
            radiant_team = game.getRadiantTeam()
            dire_team = game.getDireTeam()

            if radiant_team is not None and str(radiant_team.getTeamID()) in list_of_team_ids:
                relevantGames.append(game)
            elif dire_team is not None and str(dire_team.getTeamID()) in list_of_team_ids:
                relevantGames.append(game)

        return relevantGames

    def loadConfig(self):
        configMap = {}
        config_file = open(HelperTools.getConfigFile())
        for line in config_file:
            key = line.split(':')[0].strip()
            value = line.split(':')[1].strip()
            configMap[str(key)] = str(value)
        return configMap

    def loadTeams(self):
        teamsFile = HelperTools.getTeamsFile()
        teams_json = HelperTools.loadJsonFromFile(teamsFile)
        return teams_json

    def genereateTeamIDList(self, json_team_list):
        team_id_list = []
        for team in json_team_list:
            team_id_list.append(str(team["team_id"]))
        return team_id_list

    def loadApiKey(self):
        key_file = open(HelperTools.getApiKeyFile())
        key = key_file.read().strip()
        return key

if __name__ == '__main__':
    crawler = AtrapCrawler()
    crawler.start()
