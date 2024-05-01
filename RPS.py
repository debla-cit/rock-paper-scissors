
def player(prev_opponent_play, opponent_history=[],
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
           }], own_history=[]):
    #We implement the strategies of the 4 other opponents and we play the opposite
    #We keep tracks of our own history too
    if not own_history:
        prev_own_play = 'R'
    else:
        prev_own_play = own_history[-1]
    opponent_history.append(prev_own_play)

    last_two = "".join(own_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_own_play + "R",
        prev_own_play + "P",
        prev_own_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
    choices_quincy = ["P", "P", "S", "S", "R"]

    guess_abbey = ideal_response[prediction]
    guess_quincy = choices_quincy[(len(own_history) + 1) % len(choices_quincy)]

    last_ten = own_history[-10:]
    try:
        most_frequent = max(set(last_ten), key=last_ten.count)
    except ValueError:
        most_frequent = 'S'
    guess_mrugesh = ideal_response[most_frequent]
    try:
        guess_kris = ideal_response[own_history[-1]]
    except IndexError:
        guess_kris = 'R'

    #In all the guesses, we pick the one in majority.
    #We give more weight to the result against Abbey and Kris. They seem to be tougher than the others
    table_guess = [guess_abbey, guess_abbey, guess_abbey, guess_quincy, guess_quincy, guess_mrugesh,
                   guess_kris, guess_kris, guess_kris]

    most_frequent_guess = max(set(table_guess), key=table_guess.count)

    #We force to play the result against Abbey every 3 games
    if len(own_history) % 3 == 0:
        most_frequent_guess = guess_abbey

    own_history.append(most_frequent_guess)
    return most_frequent_guess
