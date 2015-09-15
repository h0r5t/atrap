from core import HelperTools


class LocalPlayer():

    def __init__(self, local_player_filename):
        self.json_player_data = HelperTools.loadJsonFromFile(local_player_filename)

    def isEmpty(self):
        if len(self.json_player_data) == 0:
            return True
        return False

    def getTeamName(self):
        return self.json_player_data["team_name"]

    def getPlayerName(self):
        return self.json_player_data["player_name"]

    def getAverageKDA(self):
        return self.json_player_data["average_kda"]

    def getAverageGPM(self):
        return self.json_player_data["average_gpm"]

    def getAverageLastHitsPerMinute(self):
        return self.json_player_data["average_lh_per_min"]

    def getAverageXPM(self):
        return self.json_player_data["average_xpm"]

    def getAverageTowerDamage(self):
        return self.json_player_data["average_tower_damage"]

    def getAverageHeroDamage(self):
        return self.json_player_data["average_hero_damage"]

    def getGameCount(self):
        return self.json_player_data["game_count"]

    def get10LastMatches(self):
        return self.json_player_data["last_10_matches"]
