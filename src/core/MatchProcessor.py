from core import HelperTools
import os
from core.LocalObjects import LocalPlayer
from core.LocalObjects import AverageValues
from core.LocalObjects import TeamsFile
import logging


class MatchProcessor():

    def __init__(self):
        pass

    def process(self, match_details_instance):
        teams = match_details_instance.getRadiantTeamName() + " vs " + match_details_instance.getDireTeamName()
        HelperTools.log("   processing match: " + str(match_details_instance.getMatchID()) + ": " + teams)
        for match_details_player in match_details_instance.getPlayers():
            # process player and average data
            self.processPlayer(match_details_player, self.loadLocalPlayer(str(match_details_player.getAccountID())))

        self.processMatch(match_details_instance)

    def loadLocalPlayer(self, player_id_string):
        if TeamsFile().idExists(player_id_string):
            return LocalPlayer(player_id_string)
        return None

    def processPlayer(self, match_details_player, local_player):
        if local_player is None:
            return
        player_info = local_player.getTeamName() + "." + local_player.getPlayerName()
        player_info += " (" + local_player.getPlayerPosition() + ")"
        HelperTools.log("      processing player: " + player_info)
        log = logging.getLogger("EndToEndTest")
        log.debug(local_player.getPlayerPosition())

        avg_values = AverageValues(local_player.getPlayerPosition())

        local_player.applyMatchDetails(match_details_player, avg_values)
        avg_values.applyMatchDetails(match_details_player)

        local_player.save()
        avg_values.save()

    def processMatch(self, match_details_instance):
        # TODO
        match_details_instance.save()
