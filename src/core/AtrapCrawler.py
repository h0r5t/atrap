from core.Dota2ApiWrapper import Dota2ApiWrapper
from core import HelperTools
import time
from core.MatchProcessor import MatchProcessor
import os
import json


class AtrapCrawler():
    def __init__(self):
        self.configMap = self.loadConfig()

        api_key = self.loadApiKey()
        self.api_wrapper = Dota2ApiWrapper(api_key)

        self.stopBool = False

        # list of match IDs
        self.oldRelevantGames = []

        # contains list of {"countdown": <cd>, "match_id": <match_id>, "age": <age>s}
        self.finishedGames = []

        HelperTools.log("crawler started")

    def stop(self):
        self.stopBool = True

    def start(self):
        while(True):
            teamsList = self.loadTeams()
            team_id_list = self.genereateTeamIDList(teamsList)

            try:
                currentRelevantGames = self.getRelevantLiveLeagueGames(team_id_list)
            except ApiException:
                currentRelevantGames = self.oldRelevantGames

            new_finished_games = self.findFinishedGames(self.oldRelevantGames, currentRelevantGames)
            if len(new_finished_games) > 0:
                self.finishedGames.extend(new_finished_games)

            # process matches
            match_processor = MatchProcessor()
            processed_matches = []
            to_remove_finished_games = []  # games not up after 2hrs, can remove
            for obj in self.finishedGames:
                if obj["countdown"] <= 0:
                    match_details_obj = self.api_wrapper.getMatchDetails(obj["match_id"])
                    if match_details_obj.isEmpty():
                        # match data is not available yet
                        obj["age"] = (obj["age"] + 1)
                        if obj["age"] > 60:
                            to_remove_finished_games.append(obj)
                        obj["countdown"] = int(self.configMap["match_parser_countdown"])
                        continue
                    match_processor.process(match_details_obj)
                    processed_matches.append(obj)

            # delete finished games older than 2hrs
            for obj in to_remove_finished_games:
                HelperTools.log("gave up on match " + obj["match_id"])
                self.finishedGames.remove(obj)

            # delete all parsed matches from finishedGames list
            for game in processed_matches:
                self.finishedGames.remove(game)

            # iterate cooldowns of finished gamess
            for obj in self.finishedGames:
                countdown = obj["countdown"]
                obj["countdown"] = countdown - int(self.configMap["crawler_sleep_time"])

            if self.stopBool:
                HelperTools.log("stop message received")
                break

            time.sleep(int(self.configMap["crawler_sleep_time"]))

    def findFinishedGames(self, old_relevant_games, current_relevant_games):
        finished_games = []

        for match_id in current_relevant_games:
            if match_id not in old_relevant_games:
                # relevant game just went live
                HelperTools.log("a relevant game just went live: " + str(match_id))

        for match_id in old_relevant_games:
            if match_id not in current_relevant_games:
                # relevant game is finished, can be parsed
                obj = {"countdown": int(self.configMap["match_parser_countdown"]), "match_id": match_id, "age": 0}
                finished_games.append(obj)
                HelperTools.log("a relevant game just finished: " + str(match_id))

        self.oldRelevantGames = current_relevant_games
        return finished_games

    def getRelevantLiveLeagueGames(self, list_of_relevant_team_ids):
        # IDs need to be in string format
        relevantGames = []
        liveGames = self.api_wrapper.getLiveLeagueGames()

        if liveGames is None:
            raise ApiException("api exception")

        for game in liveGames:
            radiant_team = game.getRadiantTeam()
            dire_team = game.getDireTeam()

            if radiant_team is not None and str(radiant_team.getTeamID()) in list_of_relevant_team_ids:
                relevantGames.append(game.getMatchID())
            elif dire_team is not None and str(dire_team.getTeamID()) in list_of_relevant_team_ids:
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
        teams_json = loadJsonFromFile(teamsFile)
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


class ApiException(Exception):
    pass


def loadJsonFromFile(path):
    if not os.path.isfile(path):
        return {}
    sample = open(path, encoding="utf8")
    content = sample.read().strip()
    if (content == ""):
        return {}
    json_obj = json.loads(content)
    return json_obj
