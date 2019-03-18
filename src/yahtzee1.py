#!/C/Users/djdav/PycharmProjects/yahtzee/venv/Scripts/python
import copy
from random import randint
from src import scoring1


def roll_dice(dice):
    while len(dice) < 5:
        dice.append(randint(1, 6))
    return dice


def replace_dice(dice):
    new_dice = copy.deepcopy(dice)
    roll_count = 1
    while roll_count <= 3:
        print(f'You rolled {new_dice[0]}, {new_dice[1]}, {new_dice[2]}, {new_dice[3]}, {new_dice[4]}.')
        for i, item in enumerate(new_dice):
            response = input(f'Will you keep your {item}? Type Y/N or Q to quit. ').upper()
            if response == 'Y':
                continue
            elif response == 'N':
                new_dice[i] = randint(1, 6)
            elif response == 'Q':
                break
        roll_count += 1
    print(f'Your final roll is {new_dice[0]}, {new_dice[1]}, {new_dice[2]}, {new_dice[3]}, {new_dice[4]}.')
    return new_dice


def yahtzee():
    category = input('What category are you playing? ')
    dice = []
    roll = roll_dice(dice)
    final_roll = replace_dice(roll)
    score = scoring1.get_score(category, final_roll)
    print(f'Your final score is {score}.')


yahtzee()

