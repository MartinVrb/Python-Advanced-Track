diff = 0
won_games = 0
lost_games = 0
all_games = 0

while True:
    games_counter = 0
    tournament = input()

    if tournament == "End of tournaments":
        print(f"{((won_games / all_games) * 100):.2f}% matches win")
        print(f"{((lost_games / all_games) * 100):.2f}% matches lost")
        break

    games = int(input())
    all_games += games

    while games_counter < games:
        games_counter += 1
        desi_team_score_points = int(input())
        others_team_points = int(input())

        if desi_team_score_points > others_team_points:
            won_games += 1
            diff = desi_team_score_points - others_team_points
            print(f"Game {games_counter} of tournament {tournament}: win with {diff} points.")
        else:
            lost_games += 1
            diff = others_team_points - desi_team_score_points
            print(f"Game {games_counter} of tournament {tournament}: lost with {diff} points.")
