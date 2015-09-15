from core import HelperTools
import os
from core.LocalObjects import LocalPlayer


class MatchProcessor():

    def __init__(self):
        relevant_player_ids = self.loadRelevantPlayerIDs()

    def loadRelevantPlayerIDs(self):
        id_list = []
        players_dir = HelperTools.getPlayersDir()
        for player_filename in os.listdir(players_dir):
            if player_filename.endswith(".json"):
                id_list.append(player_filename.split(".")[0])

        return id_list

    def process(self, match_details_instance):
        self.processPlayerData(match_details_instance)
        # process match data
        # process average data

    def processPlayerData(self, match_details_instance):
        for player in match_details_instance.getPlayers():
            local_player = LocalPlayer(player)
