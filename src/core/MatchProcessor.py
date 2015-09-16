from core import HelperTools
import os
from core.LocalObjects import LocalPlayer
from core.LocalObjects import AverageValues


class MatchProcessor():

    def __init__(self):
        pass

    def process(self, match_details_instance):
        for match_details_player in match_details_instance.getPlayers():
            # process player and average data
            self.processPlayer(match_details_player, self.loadLocalPlayer(str(match_details_player.getAccountID())))

        # TODO process match data

    def loadLocalPlayer(self, player_id_string):
        path = os.path.join(HelperTools.getPlayersDir(), player_id_string + ".json")
        return LocalPlayer(path)

    def processPlayer(self, match_details_player, local_player):
        avg_values = AverageValues(local_player.getPlayerPosition())
        local_player.incrementGameCount()
        avg_values.incrementGameCount()

        # TODO generate rating and set accordingly in LocalPlayer object

        local_player.save()
        avg_values.save()
