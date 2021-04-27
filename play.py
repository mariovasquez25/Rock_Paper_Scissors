def vs_player(player):
    if player.__name__ == 'leonardo':
        print('-'*64)
        print('Player 1 vs Leonardo')
    elif player.__name__ == 'raphael':
        print('-'*64)
        print('Player 1 vs Raphael')
    elif player.__name__ == 'donatello':
        print('-'*64)
        print('Player 1 vs Donatello')
    elif player.__name__ == 'michelangelo':
        print('-'*64)
        print('Player 1 vs Michelangelo')


def play(player1, player2, num_games, verbose=False):

    vs_player(player2)
    
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results["p2"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['p2'] + results['p1']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")
