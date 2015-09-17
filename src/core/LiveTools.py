from core.Dota2ApiWrapper import Dota2ApiWrapper
import time


def showLiveLeagueGames(api_key):
    api = Dota2ApiWrapper(api_key)

    # {match_id: string}
    live_games = {}
    while True:
        games_list = api.getLiveLeagueGames()
        game_ids = []
        if games_list is not None:
            for game in games_list:
                game_ids.append(int(game.getMatchID()))
                if int(game.getMatchID()) not in live_games:
                    radiant_team = game.getRadiantTeam()
                    dire_team = game.getDireTeam()
                    a = ""
                    if radiant_team is not None:
                        a += radiant_team.getTeamName()
                    else:
                        a += "[Unknown]"
                    a += " vs "
                    if dire_team is not None:
                        a += dire_team.getTeamName()
                    else:
                        a += "[Unknown]"
                    print("+   " + a)
                    live_games[int(game.getMatchID())] = a

        to_delete = []
        for key in live_games:
            if key not in game_ids:
                # game ended
                to_delete.append(key)
                print("-   " + live_games[key])

        for key in to_delete:
            del live_games[key]

        time.sleep(10)
