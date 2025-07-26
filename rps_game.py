from random import choice

choices = ['rock', 'paper', 'scissors']


def computer_choice():
    return choice(choices)


def human_choice():
    user_choice = ''
    while user_choice not in choices:
        user_choice = input(
            'enter choice of rock, paper or scissors: ').strip().lower()
    return user_choice


def play_round():
    computer = computer_choice()
    user = human_choice()
    print(f'computer played {computer}')

    if computer == user:
        return (0, 0)

    match (computer, user):
        case ('rock', 'paper'):
            print('paper wraps rock')
            return (0, 1)
        case ('rock', 'scissors'):
            print('rock smashes scissors')
            return (1, 0)
        case ('paper', 'rock'):
            print('paper wraps rock')
            return (1, 0)
        case ('paper', 'scissors'):
            print('scissors cuts paper')
            return (0, 1)
        case ('scissors', 'rock'):
            print('rock smashes scissors')
            return (0, 1)
        case ('scissors', 'paper'):
            print('scissors cuts paper')
            return (1, 0)

    return (0, 0)


def game():
    computer, user = 0, 0
    print(f'score\nuser:\t\t{user}\ncomputer:\t{computer}')

    try:
        while True:
            x, y = play_round()
            if x < y:
                print('you win this round')
            elif x > y:
                print('computer wins this round')
            else:
                print('this round is a draw')

            computer += x
            user += y
            print(f'score\nuser:\t\t{user}\ncomputer:\t{computer}')
    except KeyboardInterrupt:
        print('game interrupted')
    finally:
        result = 'user wins' if user > computer else 'computer wins' if user < computer else 'draw'
        print(f'final score:\nuser:\t\t{user}\ncomputer:\t{computer}')
        print(result)


if __name__ == "__main__":
    game()
