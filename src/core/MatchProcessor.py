from core import HelperTools
import os
from core.LocalObjects import LocalPlayer


class MatchProcessor():

    def __init__(self):
        self.relevant_player_ids = self.loadRelevantPlayerIDs()

    def loadRelevantPlayerIDs(self):
        id_list = []
        players_dir = HelperTools.getPlayersDir()
        for player_filename in os.listdir(players_dir):
            if player_filename.endswith(".json"):
                id_list.append(player_filename.split(".")[0])

        return id_list

    def process(self, match_details_instance):
        local_players = self.loadLocalPlayers()
        self.processPlayerData(match_details_instance, local_players)
        # process match data
        # process average data

    def loadLocalPlayers(self):
        local_players = []
        for playerfile in os.listdir(HelperTools.getPlayersDir()):
            if playerfile != "player_positions.json":
                path = os.path.join(HelperTools.getPlayersDir(), playerfile)
                local_players.append(LocalPlayer(path))
        return local_players

    def processPlayerData(self, match_details_instance, local_players):
        pass
