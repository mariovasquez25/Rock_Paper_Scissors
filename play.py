from RPS_utils import get_choice


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


def play(player_1, player_2, num_games, model, verbose=False):

    vs_player(player_2)

    p1_prev_play = ''
    p2_prev_play = ''

    scores = {'P1': 0, 'P2': 0, 'Tie': 0}

    for i in range(num_games):

        if len(p1_prev_play) == 0:
            p1_prev_play = get_choice()
            p2_prev_play = get_choice()

        p1_play = player_1(p2_prev_play, model=model)
        p2_play = player_2(p1_prev_play)

        if p1_play == p2_play:
            scores['Tie'] += 1
            winner = 'Tie.'

        elif (p1_play == "P" and p2_play == "R") or (p1_play == "R" and p2_play == "S") or (p1_play == "S" and p2_play == "P"):
            scores['P1'] += 1
            winner = 'Player 1 wins.'

        elif (p2_play == "P" and p1_play == "R") or (p2_play == "R" and p1_play == "S") or (p2_play == "S" and p1_play == "P"):
            scores['P2'] += 1
            winner = 'Player 2 wins.'

        if verbose:
            print('Player 1', p1_play, '| player 2:', p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_winner = scores['P1'] + scores['P2']

    if games_winner == 0:
        win_rate = 0.0
    else:
        win_rate = scores['P1'] / games_winner * 100

    print('Final results:', scores)
    print(f'Player 1 win rate: {win_rate}%')
