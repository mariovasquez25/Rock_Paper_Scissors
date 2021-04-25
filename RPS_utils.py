import random
import sklearn
from sklearn.neural_network import MLPClassifier


def str_to_list(option):
    if option == 'R':
        output = [1, 0, 0]
    elif option == 'P':
        output = [0, 1, 0]
    elif option == 'S':
        output = [0, 0, 1]

    return output


def list_to_str(option):
    if option == [1, 0, 0]:
        output = 'R'
    elif option == [0, 1, 0]:
        output = 'P'
    elif option == [0, 0, 1]:
        output = 'S'

    return output


def search_winner(p1, p2):
    if p1 == p2:
        result = 0
    elif p1 == "R" and p2 == "S":
        result = 1
    elif p1 == "R" and p2 == "P":
        result = 2
    elif p1 == "S" and p2 == "R":
        result = 2
    elif p1 == "S" and p2 == "P":
        result = 1
    elif p1 == "P" and p2 == "R":
        result = 1
    elif p1 == "P" and p2 == "S":
        result = 2

    return result


def get_choice():
    return random.choice(['R', 'S', 'P'])


def fitting():
    X = list(map(str_to_list, ['R', 'P', 'S']))
    Y = list(map(str_to_list, ['P', 'S', 'R']))

    mlp = MLPClassifier(verbose=False, warm_start=True)
    mlp.fit(X, Y)

    return mlp


def play_and_learn(iter, model):
    options = ['R', 'P', 'S']
    score = {'win': 0, 'lose': 0}

    data_x = []
    data_y = []

    for i in range(iter):
        player_1 = get_choice()

        predict = model.predict_proba([str_to_list(player_1)])[0]

        if predict[0] >= 0.95:
            player_2 = options[0]
        elif predict[1] >= 0.95:
            player_2 = options[1]
        elif predict[2] >= 0.95:
            player_2 = options[2]
        else:
            player_2 = get_choice()

        winner = search_winner(player_1, player_2)

        if winner == 2:
            data_x.append(str_to_list(player_1))
            data_y.append(str_to_list(player_2))

            score['win'] += 1
        else:
            score['lose'] += 1

    return score, data_x, data_y


def iteration_training(iter, model):
    i = 0
    historic_pct = []
    while True:
        i += 1

        score, data_x, data_y = play_and_learn(iter, model)
        pct = ((score['win']*100)/(score['win']+score['lose']))
        historic_pct.append(pct)

        if len(data_x):
            model = model.partial_fit(data_x, data_y)

        if sum(historic_pct[-9:]) == 900:
            break

    return model


def prediction(values, mlp):
    predictions = []

    for i in values:
        predict = list_to_str(list(mlp.predict([str_to_list(i)])[0]))
        predictions.append(predict)

    return predictions


def fitting_and_training(iter):
    mlp = fitting()
    print('Fitting model finished')
    mlp = iteration_training(iter, mlp)
    print('Training model finished')
    return mlp
