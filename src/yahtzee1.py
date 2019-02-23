#!/C/Users/djdav/PycharmProjects/yahtzee/venv/Scripts/python
import copy
from random import randint


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


def get_pip_count(roll):
    pip_count = {}
    for item in roll:
        pip_count[item] = roll.count(item)
    return pip_count


def get_score(category, roll):
    pip_count = get_pip_count(roll)
    score = 0
    if category.lower() == 'chance':
        return __sum_all_dice(roll)
    if category.lower() == 'yahtzee' and len(pip_count) == 1:
        score = 50
    if category.lower() == 'full house' and len(pip_count) == 2 and 3 in pip_count.values():
        score = __sum_all_dice(roll)
    if category.lower() == 'four of a kind' and len(pip_count) == 2 and 4 in pip_count.values():
        sorted_roll = sorted(roll)
        score = __get_score_from_roll(sorted_roll, sorted_roll[2])
    if category.lower() == 'large straight' and len(pip_count) == 5 and 1 not in pip_count.keys():
        score = __sum_all_dice(roll)
    if category.lower() == 'small straight' and len(pip_count) == 5 and 6 not in pip_count.keys():
        score = __sum_all_dice(roll)
    if category.lower() == 'three of a kind' and len(pip_count) == 3 and 2 not in pip_count.values():
        sorted_roll = sorted(roll)
        score = __get_score_from_roll(sorted_roll, sorted_roll[2])
    if category.lower() == 'two pairs' and len(pip_count) == 3:
        sorted_roll = sorted(roll)
        pair_one = __get_score_from_roll(sorted_roll, sorted_roll[1])
        pair_two = __get_score_from_roll(sorted_roll, sorted_roll[3])
        score = pair_one + pair_two
    if category.lower() == 'one pair' and len(pip_count) == 4:
        sorted_roll = sorted(roll)
        for item in sorted_roll:
            if sorted_roll.count(item) == 2:
                score = __get_score_from_roll(sorted_roll, sorted_roll[item])
    if category.lower() == 'sixes':
        score = __get_score_from_roll(roll, 6)
    if category.lower() == 'fives':
        score = __get_score_from_roll(roll, 5)
    if category.lower() == 'fours':
        score = __get_score_from_roll(roll, 4)
    if category.lower() == 'threes':
        score = __get_score_from_roll(roll, 3)
    if category.lower() == 'twos':
        score = __get_score_from_roll(roll, 2)
    if category.lower() == 'ones':
        score = __get_score_from_roll(roll, 1)
    return score



def __get_score_from_roll(roll, value):
    score = 0
    for item in roll:
        if item == value:
            score += value
    return score


def __sum_all_dice(dice):
    score = 0
    for num in dice:
        score += num
    return score


def yahtzee():
    dice = []
    roll = roll_dice(dice)
    replace_dice(roll)


# yahtzee()

