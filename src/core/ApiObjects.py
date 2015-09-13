class ApiObject():

    def __init__(self, json_object):
        self.json_object = json_object


class LiveLeagueGamesList(ApiObject):

    def __init__(self, json_object):
        ApiObject.__init__(self, json_object)

    def getGames(self):
        games = []
        for game in self.json_object["result"]["games"]:
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
