from models.dice import Dice
from src.scoring2 import OfAKind, Individual, Yahtzee, Straights, FullHouse, Pairs, Chance


def create_roll(num1, num2, num3, num4, num5):
    die1 = Dice()
    die1.rolled_value = num1
    die2 = Dice()
    die2.rolled_value = num2
    die3 = Dice()
    die3.rolled_value = num3
    die4 = Dice()
    die4.rolled_value = num4
    die5 = Dice()
    die5.rolled_value = num5
    return [die1, die2, die3, die4, die5]


def test_get_score__should_return_score_for_chance():
    roll = create_roll(5, 6, 5, 4, 5)
    chance = Chance(roll, 'chance')

    actual = chance.score()

    assert actual == 25


def test_get_score__should_return_score_for_yahtzee_TRUE():
    roll = create_roll(5, 5, 5, 5, 5)
    yahtzee = Yahtzee(roll, 'yahtzee')

    actual = yahtzee.score()

    assert actual == 50


def test_get_score__should_return_score_for_yahtzee_FALSE():
    roll = create_roll(5, 5, 5, 5, 4)
    yahtzee = Yahtzee(roll, 'yahtzee')

    actual = yahtzee.score()

    assert actual == 0


def test_get_score__should_return_score_for_full_house_TRUE():
    roll = create_roll(5, 4, 5, 4, 5)
    full_house = FullHouse(roll, 'full_house')

    actual = full_house.score()

    assert actual == 23


def test_get_score__should_return_score_for_full_house_FALSE():
    roll = create_roll(1, 1, 1, 1, 1)
    full_house = FullHouse(roll, 'full_house')

    actual = full_house.score()

    assert actual == 0


def test_get_score__should_return_score_for_large_straight_TRUE():
    roll = create_roll(2, 3, 4, 5, 6)
    large_straight = Straights(roll, 'large_straight')

    actual = large_straight.score()

    assert actual == 20


def test_get_score__should_return_score_for_large_straight_FALSE():
    roll = create_roll(1, 2, 1, 2, 1)
    large_straight = Straights(roll, 'large_straight')

    actual = large_straight.score()

    assert actual == 0


def test_get_score__should_return_score_for_small_straight_TRUE():
    roll = create_roll(1, 2, 3, 4, 5)
    small_straight = Straights(roll, 'small_straight')

    actual = small_straight.score()

    assert actual == 15


def test_get_score__should_return_score_for_small_straight_FALSE():
    roll = create_roll(1, 2, 1, 2, 1)
    small_straight = Straights(roll, 'small_straight')

    actual = small_straight.score()

    assert actual == 0


def test_get_score__should_return_score_for_four_of_a_kind_TRUE():
    roll = create_roll(4, 4, 4, 4, 3)
    four_of_a_kind = OfAKind(roll, 'four_of_a_kind')

    actual = four_of_a_kind.score()

    assert actual == 16


def test_get_score__should_return_score_for_four_of_a_kind_FALSE():
    roll = create_roll(4, 4, 4, 3, 3)
    four_of_a_kind = OfAKind(roll, 'four_of_a_kind')

    actual = four_of_a_kind.score()

    assert actual == 0


def test_get_score__should_return_score_for_three_of_a_kind_TRUE():
    roll = create_roll(3, 2, 2, 1, 2)
    three_of_a_kind = OfAKind(roll, 'three_of_a_kind')

    actual = three_of_a_kind.score()

    assert actual == 6


def test_get_score__should_return_score_for_three_of_a_kind_FALSE():
    roll = create_roll(3, 2, 1, 1, 2)
    three_of_a_kind = OfAKind(roll, 'three_of_a_kind')

    actual = three_of_a_kind.score()

    assert actual == 0


def test_get_score__should_return_score_for_two_pairs_TRUE():
    roll1 = create_roll(1, 1, 2, 3, 3)
    roll2 = create_roll(1, 2, 2, 3, 3)
    roll3 = create_roll(1, 1, 2, 2, 3)
    two_pairs1 = Pairs(roll1, 'two_pairs')
    two_pairs2 = Pairs(roll2, 'two_pairs')
    two_pairs3 = Pairs(roll3, 'two_pairs')

    actual1 = two_pairs1.score()
    actual2 = two_pairs2.score()
    actual3 = two_pairs3.score()

    assert actual1 == 8
    assert actual2 == 10
    assert actual3 == 6


def test_get_score__should_return_score_for_two_pairs_FALSE():
    roll = create_roll(1, 1, 2, 4, 5)
    two_pairs = Pairs(roll, 'two_pairs')

    actual = two_pairs.score()

    assert actual == 0


def test_get_score__should_return_score_for_one_pair_TRUE():
    roll1 = create_roll(1, 1, 2, 3, 4)
    roll2 = create_roll(1, 2, 2, 3, 4)
    roll3 = create_roll(1, 2, 3, 3, 4)
    roll4 = create_roll(1, 2, 3, 4, 4)

    one_pair1 = Pairs(roll1, 'one_pair')
    one_pair2 = Pairs(roll2, 'one_pair')
    one_pair3 = Pairs(roll3, 'one_pair')
    one_pair4 = Pairs(roll4, 'one_pair')

    actual1 = one_pair1.score()
    actual2 = one_pair2.score()
    actual3 = one_pair3.score()
    actual4 = one_pair4.score()

    assert actual1 == 2
    assert actual2 == 4
    assert actual3 == 6
    assert actual4 == 8


def test_get_score__should_return_score_for_one_pair_FALSE():
    roll = create_roll(1, 2, 3, 4, 5)
    one_pair = Pairs(roll, 'one_pair')

    actual = one_pair.score()

    assert actual == 0


def test_get_score__should_return_score_for_sixes_TRUE():
    roll = create_roll(6, 6, 6, 6, 5)
    sixes = Individual(roll, 'sixes')

    actual = sixes.score()

    assert actual == 24


def test_get_score__should_return_score_for_sixes_FALSE():
    roll = create_roll(1, 2, 3, 4, 5)
    sixes = Individual(roll, 'sixes')

    actual = sixes.score()

    assert actual == 0


def test_get_score__should_return_score_for_fives_TRUE():
    roll = create_roll(5, 5, 5, 5, 4)
    fives = Individual(roll, 'fives')

    actual = fives.score()

    assert actual == 20


def test_get_score__should_return_score_for_fives_FALSE():
    roll = create_roll(1, 2, 3, 4, 6)
    fives = Individual(roll, 'fives')

    actual = fives.score()

    assert actual == 0


def test_get_score__should_return_score_for_fours_TRUE():
    roll = create_roll(4, 4, 4, 4, 3)
    fours = Individual(roll, 'fours')

    actual = fours.score()

    assert actual == 16


def test_get_score__should_return_score_for_fours_FALSE():
    roll = create_roll(1, 2, 3, 5, 6)
    fours = Individual(roll, 'fours')

    actual = fours.score()

    assert actual == 0


def test_get_score__should_return_score_for_threes_TRUE():
    roll = create_roll(3, 3, 3, 3, 2)
    threes = Individual(roll, 'threes')

    actual = threes.score()

    assert actual == 12


def test_get_score__should_return_score_for_threes_FALSE():
    roll = create_roll(1, 2, 4, 5, 6)
    threes = Individual(roll, 'threes')

    actual = threes.score()

    assert actual == 0


def test_get_score__should_return_score_for_twos_TRUE():
    roll = create_roll(2, 2, 2, 2, 1)
    twos = Individual(roll, 'twos')

    actual = twos.score()

    assert actual == 8


def test_get_score__should_return_score_for_twos_FALSE():
    roll = create_roll(1, 3, 4, 5, 6)
    twos = Individual(roll, 'twos')

    actual = twos.score()

    assert actual == 0


def test_get_score__should_return_score_for_ones_TRUE():
    roll = create_roll(1, 1, 1, 1, 6)
    ones = Individual(roll, 'ones')

    actual = ones.score()

    assert actual == 4


def test_get_score__should_return_score_for_ones_FALSE():
    roll = create_roll(2, 3, 4, 5, 6)
    ones = Individual(roll, 'ones')

    actual = ones.score()

    assert actual == 0
