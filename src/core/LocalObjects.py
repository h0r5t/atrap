from core import HelperTools
import os


class LocalPlayer():

    def __init__(self, local_player_filename):
        self.local_player_filename = local_player_filename
        self.player_positions = HelperTools.loadJsonFromFile(HelperTools.getPlayerPositionsFile())
        self.json_player_data = HelperTools.loadJsonFromFile(local_player_filename)

        if self.isEmpty():
            # new player, needs to be created
            player_id = os.path.split(local_player_filename)[1].split(".")[0]
            player_pos_and_name = TeamsFile().getPlayerPositionAndName(player_id)

            self.json_player_data["player_id"] = player_id
            self.json_player_data["player_name"] = player_pos_and_name["player_name"]
            self.json_player_data["team_name"] = player_pos_and_name["team_name"]
            self.json_player_data["average_kda"] = 0
            self.json_player_data["average_gpm"] = 0
            self.json_player_data["average_lh_per_min"] = 0
            self.json_player_data["average_xpm"] = 0
            self.json_player_data["average_tower_damage"] = 0
            self.json_player_data["average_hero_damage"] = 0
            self.json_player_data["average_kda_rating"] = 0
            self.json_player_data["average_gpm_rating"] = 0
            self.json_player_data["average_lhpm_rating"] = 0
            self.json_player_data["average_xpm_rating"] = 0
            self.json_player_data["average_td_rating"] = 0
            self.json_player_data["average_hd_rating"] = 0
            self.json_player_data["game_count"] = 0
            self.json_player_data["10_last_matches"] = []

    def incrementGameCount(self):
        self.json_player_data["game_count"] = self.getGameCount() + 1

    def isEmpty(self):
        if len(self.json_player_data) == 0:
            return True
        return False

    def getPlayerPosition(self):
        return self.player_positions[str()]

    def getTeamName(self):
        return self.json_player_data["team_name"]

    def getPlayerName(self):
        return self.json_player_data["player_name"]

    def getPlayerID(self):
        return self.json_player_data["player_id"]

    def getAverageKDA(self):
        return self.json_player_data["average_kda"]

    def getAverageKDARating(self):
        return self.json_avg_data["average_kda_rating"]

    def getAverageGPM(self):
        return self.json_player_data["average_gpm"]

    def getAverageGPMRating(self):
        return self.json_avg_data["average_gpm_rating"]

    def getAverageLHPM(self):
        return self.json_player_data["average_lh_per_min"]

    def getAverageLastHitsPerMinuteRating(self):
        return self.json_avg_data["average_lhpm_rating"]

    def getAverageXPM(self):
        return self.json_player_data["average_xpm"]

    def getAverageXPMRating(self):
        return self.json_avg_data["average_xpm_rating"]

    def getAverageTowerDamage(self):
        return self.json_player_data["average_tower_damage"]

    def getAverageTowerDamageRating(self):
        return self.json_avg_data["average_td_rating"]

    def getAverageHeroDamage(self):
        return self.json_player_data["average_hero_damage"]

    def getAverageHeroDamageRating(self):
        return self.json_avg_data["average_hd_rating"]

    def getAverageFightRating(self):
        return self.json_avg_data["average_fight_rating"]

    def getAverageFarmRating(self):
        return self.json_avg_data["average_farm_rating"]

    def getAveragePushRating(self):
        return self.json_avg_data["average_push_rating"]

    def getAverageTotalRating(self):
        return self.json_avg_data["average_total_rating"]

    def getGameCount(self):
        return self.json_player_data["game_count"]

    def get10LastMatches(self):
        return self.json_player_data["last_10_matches"]

    def save(self):
        HelperTools.saveJsonToFile(self.json_player_data, self.local_player_filename)


class AverageValues():

    def __init__(self, player_position):
        self.avg_values_file = os.path.join(HelperTools.getWebDir, "avg", player_position, "average_values.json")
        self.json_avg_data = HelperTools.loadJsonFromFile(self.avg_values_file)

        if self.isEmpty():
            # instantiate avg file
            self.json_avg_data["average_kda"] = 0
            self.json_avg_data["average_gpm"] = 0
            self.json_avg_data["average_lh_per_min"] = 0
            self.json_avg_data["average_xpm"] = 0
            self.json_avg_data["average_tower_damage"] = 0
            self.json_avg_data["average_hero_damage"] = 0
            self.json_avg_data["game_count"] = 0

    def isEmpty(self):
        if len(self.json_avg_data) == 0:
            return True
        return False

    def incrementGameCount(self):
        self.json_avg_data["game_count"] = self.getGameCount() + 1

    def getAverageKDA(self):
        return self.json_avg_data["average_kda"]

    def getAverageGPM(self):
        return self.json_avg_data["average_gpm"]

    def getAverageLHPM(self):
        return self.json_avg_data["average_lh_per_min"]

    def getAverageXPM(self):
        return self.json_avg_data["average_xpm"]

    def getAverageTowerDamage(self):
        return self.json_avg_data["average_tower_damage"]

    def getAverageHeroDamage(self):
        return self.json_avg_data["average_hero_damage"]

    def getGameCount(self):
        return self.json_avg_data["game_count"]

    def save(self):
        HelperTools.saveJsonToFile(self.json_avg_data, self.avg_values_file)


class TeamsFile():

    def __init__(self):
        self.teams_data = HelperTools.loadJsonFromFile(HelperTools.getTeamsFile())

    def getPlayerPositionAndName(self, player_id):
        result = {}
        for team in self.teams_data:
                for player in team["players"]:
                    if player["player_id"] == int(player_id):
                        result["player_position"] = player["player_position"]
                        result["player_name"] = player["player_name"]
                        result["team_name"] = team["team_name"]
                        break

        return result
