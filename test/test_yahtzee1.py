from src import yahtzee1


def test_roll_dice__should_generate_list_of_five_integers():
    dice = []

    actual = yahtzee1.roll_dice(dice)

    assert len(actual) == 5


# def test_replace_dice__should_replace_unwanted_dice():
#     dice = [2, 3, 6, 4, 2]
#
#     actual = yahtzee1.replace_dice(dice)
#
#     assert actual is not dice
#     assert len(actual) == 5


