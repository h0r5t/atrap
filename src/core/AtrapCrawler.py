from core.Dota2ApiWrapper import Dota2ApiWrapper
from core import HelperTools
import time
from core.MatchProcessor import MatchProcessor


class AtrapCrawler():
    def __init__(self):
        self.configMap = self.loadConfig()
        api_key = self.loadApiKey()
        self.api_wrapper = Dota2ApiWrapper(api_key)

        # list of match IDs
        self.oldRelevantGames = []

        # contains list of {"countdown": <cd>, "match_id": <match_id>}
        self.finishedGames = []

    def start(self):
        while(True):

            # load static content
            teamsList = self.loadTeams()
            team_id_list = self.genereateTeamIDList(teamsList)

            currentRelevantGames = self.getRelevantLiveLeagueGames(team_id_list)
            new_finished_games = self.findFinishedGames(currentRelevantGames)
            self.finishedGames.append(new_finished_games)

            # process matches
            match_processor = MatchProcessor()
            for obj in self.finishedGames:
                if (int(obj["countdown"]) <= 0):
                    match_details_obj = self.api_wrapper.getMatchDetails(obj["match_id"])
                    match_processor.process(match_details_obj)

            # iterate cooldowns of finished gamess
            for obj in self.finishedGames:
                countdown = int(obj["countdown"])
                obj["countdown"] = countdown - int(self.configMap["crawler_sleep_time"])

            time.sleep(int(self.configMap["crawler_sleep_time"]))

    def findFinishedGames(self, old_relevant_games, current_relevant_games):
        finished_games = []
        for match_id in old_relevant_games:
            if match_id not in current_relevant_games:
                # relevant game is finished, can be parsed
                obj = {"countdown": int(self.configMap["match_parser_countdown"]), "match_id": match_id}
                finished_games.append(obj)

        self.oldRelevantGames = current_relevant_games
        return finished_games

    def getRelevantLiveLeagueGames(self, list_of_team_ids):
        # IDs need to be in string format
        relevantGames = []
        liveGames = self.api_wrapper.getLiveLeagueGames()

        for game in liveGames:
            radiant_team = game.getRadiantTeam()
            dire_team = game.getDireTeam()

            if radiant_team is not None and str(radiant_team.getTeamID()) in list_of_team_ids:
                relevantGames.append(game.getMatchID())
            elif dire_team is not None and str(dire_team.getTeamID()) in list_of_team_ids:
                relevantGames.append(game.getMatchID())

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
