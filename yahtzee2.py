#!/C/Users/djdav/Development/Python/yahtzee/venv/Scripts/python

from random import randint
from models.dice import Dice
from src.scoring2 import get_score


def play_yahtzee():
    yahtzee = Yahtzee()
    roll_count = 0

    while roll_count < 3:
        yahtzee.roll_dice()
        yahtzee.keep_roll()
        roll_count += 1
    print(f'Final Rolls: {yahtzee.roll}')
    category = input('What category are you playing? ')
    score_card = get_score(category, yahtzee.roll)
    print(f'Your score is {score_card.score()}')


class Yahtzee:
    def __init__(self):
        self.roll = [Dice(), Dice(), Dice(), Dice(), Dice()]

    def roll_dice(self):
        for dice in self.roll:
            if not dice.keep_value:
                dice.rolled_value = randint(1, 6)

    def keep_roll(self):
        print(f'You rolled {self.roll[0]}, {self.roll[1]}, {self.roll[2]}, {self.roll[3]}, {self.roll[4]}.')
        for dice in self.roll:
            response = input(f'Will you keep your {dice}? Type Y/N. ')
            dice.keep_value = True if response.upper() == 'Y' else False

    def sum_dice(self):
        total = 0
        for num in self.roll:
            total += num
        return total


play_yahtzee()
