wtf = {}

def player(prev_play, opponent_history=[]):
    global wtf

    n = 5

    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    guess = "R"  # default, until statistic kicks in

    if len(opponent_history) > n:
        inp = "".join(opponent_history[-n:])

        if "".join(opponent_history[-(n+1):]) in wtf.keys():
            wtf["".join(opponent_history[-(n+1):])] += 1
        else:
            wtf["".join(opponent_history[-(n+1):])] = 1

        possible = [inp+"R", inp+"P", inp+"S"]

        for i in possible:
            if not i in wtf.keys():
                wtf[i] = 0

        predict = max(possible, key=lambda key: wtf[key])

        if predict[-1] == "P":
            guess = "S"
        if predict[-1] == "R":
            guess = "P"
        if predict[-1] == "S":
            guess = "R"

    return guess


def leonardo(prev_play, counter=[0]):

    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def raphael(prev_opponent_play, opponent_history=[]):
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[most_frequent]


def donatello(prev_opponent_play):
    if prev_opponent_play == '':
        prev_opponent_play = "R"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prev_opponent_play]


def michelangelo(prev_opponent_play,
                 opponent_history=[],
                 play_order=[{
                     "RR": 0,
                     "RP": 0,
                     "RS": 0,
                     "PR": 0,
                     "PP": 0,
                     "PS": 0,
                     "SR": 0,
                     "SP": 0,
                     "SS": 0,
                 }]):

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
