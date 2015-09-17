class Rating():

    def __init__(self, player_position):
        self.rating_data = {}
        self.player_pos = player_position

    def calculateKDARating(self, player_kda, average_kda):
        rating = self.keepInBounds(50 + 25*(player_kda - average_kda))
        self.rating_data["kda_rating"] = rating

    def calculateGPMRating(self, player_gpm, average_gpm):
        rating = self.keepInBounds(50 + 0.15*(player_gpm - average_gpm))
        self.rating_data["gpm_rating"] = rating

    def calculateXPMRating(self, player_xpm, average_xpm):
        rating = self.keepInBounds(50 + 0.15*(player_xpm - average_xpm))
        self.rating_data["xpm_rating"] = rating

    def calculateLHPMRating(self, player_lhpm, average_lhpm):
        rating = self.keepInBounds(50 + 7.5*(player_lhpm - average_lhpm))
        self.rating_data["lhpm_rating"] = rating

    def calculateTDRating(self, player_td, average_td):
        rating = self.keepInBounds(50 + (player_td - average_td))
        self.rating_data["td_rating"] = rating

    def calculateHDRating(self, player_hd, average_hd):
        rating = self.keepInBounds(50 + 0.1*(player_hd - average_hd))
        self.rating_data["hd_rating"] = rating

    def calculateFightRating(self):
        rating = (self.rating_data["kda_rating"] + self.rating_data["hd_rating"]) / 2
        self.rating_data["fight_rating"] = rating

    def calculateFarmRating(self):
        rating = (self.rating_data["gpm_rating"] + self.rating_data["xpm_rating"]) / 2
        self.rating_data["farm_rating"] = rating

    def calculatePushRating(self):
        rating = self.rating_data["td_rating"]
        self.rating_data["push_rating"] = rating

    def calculateTotalRating(self):
        fight_q = 0.4
        push_q = 0.3
        farm_q = 0.3

        if self.player_pos == "carry":
            fight_q = 0.4
            push_q = 0.3
            farm_q = 0.3
        elif self.player_pos == "mid":
            fight_q = 0.4
            push_q = 0.2
            farm_q = 0.4
        elif self.player_pos == "offlane":
            fight_q = 0.6
            push_q = 0.1
            farm_q = 0.3
        elif self.player_pos == "support":
            fight_q = 0.6
            push_q = 0.2
            farm_q = 0.2

        fight_a = fight_q * self.rating_data["fight_rating"]
        push_a = push_q * self.rating_data["push_rating"]
        farm_a = farm_q * self.rating_data["farm_rating"]

        self.rating_data["total_rating"] = fight_a + push_a + farm_a

    def keepInBounds(self, num):
        if num > 100:
            return 100
        if num < 0:
            return 0
        return num

    def getRatings(self):
        return self.rating_data


class MatchDetailsPlayerRating(Rating):

    def __init__(self, match_details_player_instance, avg_values):
        Rating.__init__(self, avg_values.getPlayerPosition())
        self.player = match_details_player_instance
        self.calculateKDARating(self.player.getKDA(), avg_values.getAverageKDA())
        self.calculateGPMRating(self.player.getGPM(), avg_values.getAverageGPM())
        self.calculateXPMRating(self.player.getXPM(), avg_values.getAverageXPM())
        self.calculateLHPMRating(self.player.getLastHitsPerMinute(), avg_values.getAverageLHPM())
        self.calculateTDRating(self.player.getTowerDamage(), avg_values.getAverageTowerDamage())
        self.calculateHDRating(self.player.getHeroDamage(), avg_values.getAverageHeroDamage())

        self.calculateFarmRating()
        self.calculateFightRating()
        self.calculatePushRating()
        self.calculateTotalRating()
