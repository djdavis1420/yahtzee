def get_score(category, roll):
    pip_count = __get_pip_count(roll)
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


def __get_pip_count(roll):
    pip_count = {}
    for item in roll:
        pip_count[item] = roll.count(item)
    return pip_count


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
