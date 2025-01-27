a_team = list(range(1, 12))
b_team = list(range(1, 12))
sent_off_players_list = input().split()
if sent_off_players_list:
    for current_players_stats in sent_off_players_list:
        team, player = current_players_stats.split("-")
        player = int(player)

        if team == "A":
            if player in a_team:
                a_team.remove(player)
        elif team == "B":
            if player in b_team:
                b_team.remove(player)

        if len(a_team) < 7 or len(b_team) < 7:
            print(f"Team A - {len(a_team)}", end="; ")
            print(f"Team B - {len(b_team)}")
            print("Game was terminated")
            exit()

print(f"Team A - {len(a_team)}", end="; ")
print(f"Team B - {len(b_team)}")
# A-1 A-5 A-10 B-2
# Team A - 8; Team B - 10

# Team A - 6; Team B - 10
# Game was terminated
