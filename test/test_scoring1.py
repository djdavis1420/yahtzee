from src import scoring1


def test_get_pip_count__should_return_dictionary_of_pip_count():
    roll1 = [2, 3, 2, 2, 3]
    roll2 = [2, 4, 3, 5, 5]

    actual1 = scoring1.__get_pip_count(roll1)
    actual2 = scoring1.__get_pip_count(roll2)

    assert actual1 == {2: 3, 3: 2}
    assert actual2 == {2: 1, 4: 1, 3: 1, 5: 2}


def test_get_score__should_return_score_for_chance():
    roll = [5, 6, 5, 4, 5]

    actual = scoring1.get_score('chance', roll)

    assert actual == 25


def test_get_score__should_return_score_for_yahtzee_TRUE():
    roll = [5, 5, 5, 5, 5]

    actual = scoring1.get_score('yahtzee', roll)

    assert actual == 50

def test_get_score__should_return_score_for_yahtzee_FALSE():
    roll = [5, 5, 5, 5, 4]

    actual = scoring1.get_score('yahtzee', roll)

    assert actual == 0


def test_get_score__should_return_score_for_full_house_TRUE():
    roll = [5, 4, 5, 4, 5]

    actual = scoring1.get_score('full house', roll)

    assert actual == 23

def test_get_score__should_return_score_for_full_house_FALSE():
    roll = [1, 1, 1, 1, 1]

    actual = scoring1.get_score('full house', roll)

    assert actual == 0


def test_get_score__should_return_score_for_large_straight_TRUE():
    roll = [2, 3, 4, 5, 6]

    actual = scoring1.get_score('large straight', roll)

    assert actual == 20


def test_get_score__should_return_score_for_large_straight_FALSE():
    roll = [1, 2, 1, 2, 1]

    actual = scoring1.get_score('large straight', roll)

    assert actual == 0


def test_get_score__should_return_score_for_small_straight_TRUE():
    roll = [1, 2, 3, 4, 5]

    actual = scoring1.get_score('small straight', roll)

    assert actual == 15


def test_get_score__should_return_score_for_small_straight_FALSE():
    roll = [1, 2, 1, 2, 1]

    actual = scoring1.get_score('small straight', roll)

    assert actual == 0


def test_get_score__should_return_score_for_four_of_a_kind_TRUE():
    roll = [4, 4, 4, 4, 3]

    actual = scoring1.get_score('four of a kind', roll)

    assert actual == 16


def test_get_score__should_return_score_for_four_of_a_kind_FALSE():
    roll = [4, 4, 4, 3, 3]

    actual = scoring1.get_score('four of a kind', roll)

    assert actual == 0


def test_get_score__should_return_score_for_three_of_a_kind_TRUE():
    roll = [3, 2, 2, 1, 2]

    actual = scoring1.get_score('three of a kind', roll)

    assert actual == 6


def test_get_score__should_return_score_for_three_of_a_kind_FALSE():
    roll = [3, 2, 1, 1, 2]

    actual = scoring1.get_score('three of a kind', roll)

    assert actual == 0


def test_get_score__should_return_score_for_two_pairs_TRUE():
    roll1 = [1, 1, 2, 3, 3]
    roll2 = [1, 2, 2, 3, 3]
    roll3 = [1, 1, 2, 2, 3]

    actual1 = scoring1.get_score('two pairs', roll1)
    actual2 = scoring1.get_score('two pairs', roll2)
    actual3 = scoring1.get_score('two pairs', roll3)

    assert actual1 == 8
    assert actual2 == 10
    assert actual3 == 6


def test_get_score__should_return_score_for_two_pairs_FALSE():
    roll = [1, 1, 2, 4, 5]

    actual = scoring1.get_score('two pairs', roll)

    assert actual == 0


def test_get_score__should_return_score_for_one_pair_TRUE():
    roll1 = [1, 1, 2, 3, 4]
    roll2 = [1, 2, 2, 3, 4]
    roll3 = [1, 2, 3, 3, 4]
    roll4 = [1, 2, 3, 4, 4]

    actual1 = scoring1.get_score('one pair', roll1)
    actual2 = scoring1.get_score('one pair', roll2)
    actual3 = scoring1.get_score('one pair', roll3)
    actual4 = scoring1.get_score('one pair', roll4)

    assert actual1 == 2
    assert actual2 == 4
    assert actual3 == 6
    assert actual4 == 8


def test_get_score__should_return_score_for_one_pair_FALSE():
    roll = [1, 2, 3, 4, 5]

    actual = scoring1.get_score('one pair', roll)

    assert actual == 0


def test_get_score__should_return_score_for_sixes_TRUE():
    roll = [6, 6, 6, 6, 5]

    actual = scoring1.get_score('sixes', roll)

    assert actual == 24


def test_get_score__should_return_score_for_sixes_FALSE():
    roll = [1, 2, 3, 4, 5]

    actual = scoring1.get_score('sixes', roll)

    assert actual == 0


def test_get_score__should_return_score_for_fives_TRUE():
    roll = [5, 5, 5, 5, 4]

    actual = scoring1.get_score('fives', roll)

    assert actual == 20


def test_get_score__should_return_score_for_fives_FALSE():
    roll = [1, 2, 3, 4, 6]

    actual = scoring1.get_score('fives', roll)

    assert actual == 0



def test_get_score__should_return_score_for_fours_TRUE():
    roll = [4, 4, 4, 4, 3]

    actual = scoring1.get_score('fours', roll)

    assert actual == 16


def test_get_score__should_return_score_for_fours_FALSE():
    roll = [1, 2, 3, 5, 6]

    actual = scoring1.get_score('fours', roll)

    assert actual == 0


def test_get_score__should_return_score_for_threes_TRUE():
    roll = [3, 3, 3, 3, 2]

    actual = scoring1.get_score('threes', roll)

    assert actual == 12


def test_get_score__should_return_score_for_threes_FALSE():
    roll = [1, 2, 4, 5, 6]

    actual = scoring1.get_score('threes', roll)

    assert actual == 0


def test_get_score__should_return_score_for_twos_TRUE():
    roll = [2, 2, 2, 2, 1]

    actual = scoring1.get_score('twos', roll)

    assert actual == 8


def test_get_score__should_return_score_for_twos_FALSE():
    roll = [1, 3, 4, 5, 6]

    actual = scoring1.get_score('twos', roll)

    assert actual == 0


def test_get_score__should_return_score_for_ones_TRUE():
    roll = [1, 1, 1, 1, 6]

    actual = scoring1.get_score('ones', roll)

    assert actual == 4


def test_get_score__should_return_score_for_ones_FALSE():
    roll = [2, 3, 4, 5, 6]

    actual = scoring1.get_score('ones', roll)

    assert actual == 0


def test_sum_dice__should_return_sum_of_all_dice():
    dice = [5, 3, 1, 2, 4]

    actual = scoring1.__sum_all_dice(dice)

    assert actual == 15

