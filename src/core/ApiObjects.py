class ApiObject():

    def __init__(self, json_object):
        self.json_object = json_object


class LiveLeagueGamesList(ApiObject):

    def __init__(self, json_object):
        ApiObject.__init__(self, json_object["result"])

    def getGames(self):
        games = []
        for game in self.json_object["games"]:
            games.append(LiveLeagueGame(game))
        return games


class LiveLeagueGame(ApiObject):

    def __init__(self, json_object):
        ApiObject.__init__(self, json_object)

    def getMatchID(self):
        return str(self.json_object["match_id"])

    def getRadiantTeam(self):
        if "radiant_team" in self.json_object:
            return LiveLeagueGameTeam(self.json_object["radiant_team"])
        return None

    def getDireTeam(self):
        if "dire_team" in self.json_object:
            return LiveLeagueGameTeam(self.json_object["dire_team"])
        return None


class LiveLeagueGameTeam(ApiObject):

    def __init__(self, json_object):
        ApiObject.__init__(self, json_object)

    def getTeamName(self):
        return self.json_object["team_name"]

    def getTeamID(self):
        return str(self.json_object["team_id"])


class MatchDetails(ApiObject):

    def __init__(self, json_object):
        ApiObject.__init__(self, json_object["result"])
        self.players = []
        for player in self.json_object["players"]:
            self.players.append(MatchDetailsPlayer(player))

    def getPlayers(self):
        return self.players

    def getMatchID(self):
        return str(self.json_object["match_id"])

    def getLeagueID(self):
        return str(self.json_object["leagueid"])

    def getRadiantWin(self):
        return bool(self.json_object["radiant_win"])

    def getMatchLength(self):
        return str(self.json_object["duration"])


class MatchDetailsPlayer(ApiObject):

    def __init__(self, json_object):
        ApiObject.__init__(self, json_object)

    def getAccountID(self):
        return str(self.json_object["account_id"])

    def wasOnRadiant(self):
        player_slot = self.json_object["player_slot"]
        if ((player_slot & (1 << 7)) != 0) == 1:
            return False
        return True

    def getKills(self):
        return str(self.json_object["kills"])

    def getDeaths(self):
        return str(self.json_object["deaths"])

    def getAssists(self):
        return str(self.json_object["assists"])

    def getLastHits(self):
        return str(self.json_object["last_hits"])

    def getGPM(self):
        return str(self.json_object["gold_per_min"])

    def getXPM(self):
        return str(self.json_object["xp_per_min"])

    def getTowerDamage(self):
        return str(self.json_object["tower_damage"])

    def getHeroDamage(self):
        return str(self.json_object["hero_damage"])

    def getHeroHealing(self):
        return str(self.json_object["hero_healing"])
