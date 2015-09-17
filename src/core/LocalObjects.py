from core import HelperTools
import os
from core.PlayerRating import MatchDetailsPlayerRating
import json


class LocalPlayer():

    def __init__(self, player_id):
        self.local_player_filename = os.path.join(HelperTools.getWebDir(), "live", "players", str(player_id) + ".json")
        self.json_player_data = loadJsonFromFile(self.local_player_filename)
        self.isAnonymous = False

        if self.isEmpty():
            # new player, needs to be created
            player_pos_and_name = TeamsFile().getPlayerPositionAndName(player_id)
            player_pos = player_pos_and_name["player_position"]
            player_name = player_pos_and_name["player_name"]
            team_name = player_pos_and_name["team_name"]

            self.json_player_data["player_id"] = player_id
            self.json_player_data["player_name"] = player_name
            self.json_player_data["player_position"] = player_pos
            self.json_player_data["team_name"] = team_name
            self.json_player_data["average_kda"] = 0
            self.json_player_data["average_gpm"] = 0
            self.json_player_data["average_lh_per_min"] = 0
            self.json_player_data["average_xpm"] = 0
            self.json_player_data["average_tower_damage"] = 0
            self.json_player_data["average_hero_damage"] = 0
            self.json_player_data["average_kda_rating"] = 50
            self.json_player_data["average_gpm_rating"] = 50
            self.json_player_data["average_lhpm_rating"] = 50
            self.json_player_data["average_xpm_rating"] = 50
            self.json_player_data["average_td_rating"] = 50
            self.json_player_data["average_hd_rating"] = 50
            self.json_player_data["average_fight_rating"] = 50
            self.json_player_data["average_push_rating"] = 50
            self.json_player_data["average_farm_rating"] = 50
            self.json_player_data["average_total_rating"] = 50
            self.json_player_data["counter"] = 0
            self.json_player_data["10_last_matches"] = []

    def incrementCounter(self):
        self.json_player_data["counter"] = self.getCounter() + 1

    def isEmpty(self):
        if len(self.json_player_data) == 0:
            return True
        return False

    def applyMatchDetails(self, match_details_player, avg_values_instance):
        self.updateAverageWithName("average_kda", match_details_player.getKDA())
        HelperTools.log("           kda: " + str(match_details_player.getKDA()))
        self.updateAverageWithName("average_gpm", match_details_player.getGPM())
        HelperTools.log("           gpm: " + str(match_details_player.getGPM()))
        self.updateAverageWithName("average_lh_per_min", match_details_player.getLastHitsPerMinute())
        HelperTools.log("           lhpm: " + str(match_details_player.getLastHitsPerMinute()))
        self.updateAverageWithName("average_xpm", match_details_player.getXPM())
        HelperTools.log("           xpm: " + str(match_details_player.getXPM()))
        self.updateAverageWithName("average_hero_damage", match_details_player.getHeroDamage())
        HelperTools.log("           hd: " + str(match_details_player.getHeroDamage()))
        self.updateAverageWithName("average_tower_damage", match_details_player.getTowerDamage())
        HelperTools.log("           td: " + str(match_details_player.getTowerDamage()))

        rating = MatchDetailsPlayerRating(match_details_player, avg_values_instance)
        self.applyRating(rating)

        self.incrementCounter()

    def applyRating(self, rating):
        rating_data = rating.getRatings()
        self.updateAverageWithName("average_kda_rating", rating_data["kda_rating"])
        HelperTools.log("           kda_rating: " + str(rating_data["kda_rating"]))
        self.updateAverageWithName("average_gpm_rating", rating_data["gpm_rating"])
        HelperTools.log("           gpm_rating: " + str(rating_data["gpm_rating"]))
        self.updateAverageWithName("average_lhpm_rating", rating_data["lhpm_rating"])
        HelperTools.log("           lhpm_rating: " + str(rating_data["lhpm_rating"]))
        self.updateAverageWithName("average_xpm_rating", rating_data["xpm_rating"])
        HelperTools.log("           xpm_rating: " + str(rating_data["xpm_rating"]))
        self.updateAverageWithName("average_hd_rating", rating_data["hd_rating"])
        HelperTools.log("           hd_rating: " + str(rating_data["hd_rating"]))
        self.updateAverageWithName("average_td_rating", rating_data["td_rating"])
        HelperTools.log("           td_rating: " + str(rating_data["td_rating"]))
        self.updateAverageWithName("average_fight_rating", rating_data["fight_rating"])
        HelperTools.log("           fight_rating: " + str(rating_data["fight_rating"]))
        self.updateAverageWithName("average_push_rating", rating_data["push_rating"])
        HelperTools.log("           push_rating: " + str(rating_data["push_rating"]))
        self.updateAverageWithName("average_farm_rating", rating_data["farm_rating"])
        HelperTools.log("           farm_rating: " + str(rating_data["farm_rating"]))
        self.updateAverageWithName("average_total_rating", rating_data["total_rating"])
        HelperTools.log("           total_rating: " + str(rating_data["total_rating"]))
        HelperTools.log("")

    def updateAverageWithName(self, name, value):
        old_avg = int(self.json_player_data[name])
        new_avg = updateAverage(old_avg, self.getCounter(), value)
        self.json_player_data[name] = new_avg

    def getPlayerPosition(self):
        return self.json_player_data["player_position"]

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

    def getCounter(self):
        return self.json_player_data["counter"]

    def get10LastMatches(self):
        return self.json_player_data["last_10_matches"]

    def save(self):
        saveJsonToFile(self.json_player_data, self.local_player_filename)


class AverageValues():

    def __init__(self, player_position):
        self.player_pos = player_position
        self.avg_values_file = os.path.join(HelperTools.getWebDir(), "avg", player_position, "average_values.json")
        self.json_avg_data = loadJsonFromFile(self.avg_values_file)

        if self.isEmpty():
            # instantiate avg file
            self.json_avg_data["average_kda"] = 2.5
            self.json_avg_data["average_gpm"] = 400
            self.json_avg_data["average_lh_per_min"] = 5
            self.json_avg_data["average_xpm"] = 400
            self.json_avg_data["average_tower_damage"] = 25
            self.json_avg_data["average_hero_damage"] = 250
            self.json_avg_data["counter"] = 0

    def getPlayerPosition(self):
        return self.player_pos

    def isEmpty(self):
        if len(self.json_avg_data) == 0:
            return True
        return False

    def incrementCounter(self):
        self.json_avg_data["counter"] = self.getCounter() + 1

    def applyMatchDetails(self, match_details_player):
        self.updateAverageWithName("average_kda", match_details_player.getKDA())
        self.updateAverageWithName("average_gpm", match_details_player.getGPM())
        self.updateAverageWithName("average_lh_per_min", match_details_player.getLastHitsPerMinute())
        self.updateAverageWithName("average_xpm", match_details_player.getXPM())
        self.updateAverageWithName("average_hero_damage", match_details_player.getHeroDamage())
        self.updateAverageWithName("average_tower_damage", match_details_player.getTowerDamage())

        self.incrementCounter()

    def updateAverageWithName(self, name, value):
        old_avg = int(self.json_avg_data[name])
        new_avg = updateAverage(old_avg, self.getCounter(), value)
        self.json_avg_data[name] = new_avg

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

    def getCounter(self):
        return self.json_avg_data["counter"]

    def save(self):
        saveJsonToFile(self.json_avg_data, self.avg_values_file)


class TeamsFile():

    def __init__(self):
        self.teams_data = loadJsonFromFile(HelperTools.getTeamsFile())

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

    def idExists(self, player_id):
        found = False
        for team in self.teams_data:
                for player in team["players"]:
                    if player["player_id"] == int(player_id):
                        found = True
                        break

        return found


def updateAverage(old_average, counter, value):
    new_average = ((old_average * counter) + value) / (counter + 1)
    return new_average


def loadJsonFromFile(path):
    if not os.path.isfile(path):
        return {}
    sample = open(path, encoding="utf8")
    content = sample.read().strip()
    if (content == ""):
        return {}
    json_obj = json.loads(content)
    return json_obj


def saveJsonToFile(json_obj, path):
    with open(path, "w") as f:
        f.truncate()
        json.dump(json_obj, f, sort_keys=True, indent=4, separators=(',', ': '))
