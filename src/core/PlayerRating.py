class Rating():

    def __init__(self):
        self.rating_data = {}

    def calculateKDARating(self, player_kda, average_kda):
        rating = 0
        self.rating_data["kda_rating"] = rating

    def calculateGPMRating(self, player_gpm, average_gpm):
        rating = 0
        self.rating_data["gpm_rating"] = rating

    def calculateXPMRating(self, player_xpm, average_xpm):
        rating = 0
        self.rating_data["xpm_rating"] = rating

    def calculateLHPMRating(self, player_lhpm, average_lhpm):
        rating = 0
        self.rating_data["lhpm_rating"] = rating

    def calculateTDRating(self, player_td, average_td):
        rating = 0
        self.rating_data["td_rating"] = rating

    def calculateHDRating(self, player_hd, average_hd):
        rating = 0
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
        # TODO rate after design
        self.rating_data["total_rating"] = 50

    def getRatings(self):
        return self.rating_data


class MatchDetailsPlayerRating(Rating):

    def __init__(self, match_details_player_instance, avg_values):
        Rating.__init__(self)
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
