from abc import abstractmethod
from statistics import mode, StatisticsError


def get_score(category, roll):
    if category == 'chance':
        return Chance(roll, category)
    if category == 'yahtzee':
        return Yahtzee(roll, category)
    if category == 'full_house':
        return FullHouse(roll, category)
    if 'straight' in category:
        return Straights(roll, category)
    if 'of_a_kind' in category:
        return OfAKind(roll, category)
    if 'pair' in category:
        return Pairs(roll, category)
    else:
        return Individual(roll, category)


CATEGORY = {
    'chance': None,
    'yahtzee': 5,
    'full_house': None,
    'large_straight': 1,
    'small_straight': 6,
    'four_of_a_kind': 4,
    'three_of_a_kind': 3,
    'two_pairs': None,
    'one_pair': None,
    'sixes': 6,
    'fives': 5,
    'fours': 4,
    'threes': 3,
    'twos': 2,
    'ones': 1
}


class Category:
    def __init__(self, roll, category):
        self.roll = roll
        self.category = category
        self.dice_values = [item.rolled_value for item in self.roll]

    @abstractmethod
    def score(self):
        pass


class Chance(Category):
    def score(self):
        return sum(self.dice_values)


class Yahtzee(Category):
    def score(self):
        matching_die = [die for die in self.dice_values if die == CATEGORY.get(self.category)]
        return 50 if len(matching_die) == CATEGORY.get(self.category) else 0


class FullHouse(Category):
    def score(self):
        return sum(self.dice_values) if len(set(self.dice_values)) == 2 else 0


class Straights(Category):
    def score(self):
        small = {1, 2, 3, 4, 5}
        large = {2, 3, 4, 5, 6}
        rollset = set(self.dice_values)

        if len(small.difference(rollset)) == 0 and CATEGORY.get(self.category) not in rollset:
            return 15
        elif len(large.difference(rollset)) == 0 and CATEGORY.get(self.category) not in rollset:
            return 20
        else:
            return 0


class OfAKind(Category):
    def score(self):
        try:
            most_common = mode(self.dice_values)
            matching_die = [die for die in self.dice_values if die == most_common]
            if self.category == 'four_of_a_kind' and len(matching_die) == 4:
                return sum(matching_die)
            if self.category == 'three_of_a_kind' and len(matching_die) == 3:
                return sum(matching_die)
            return 0
        except StatisticsError:
            return 0


class Pairs(Category):
    def score(self):
        if self.category == 'two_pairs' and len(set(self.dice_values)) == 3:
            sorted_roll = sorted(self.dice_values)
            return (sorted_roll[1] * 2) + (sorted_roll[3] * 2)
        if self.category == 'one_pair' and len(set(self.dice_values)) == 4:
            sorted_roll = sorted(self.dice_values)
            for item in sorted_roll:
                if sorted_roll.count(item) == 2:
                    return item * 2
        return 0


class Individual(Category):
    def score(self):
        matching_die = [die for die in self.dice_values if die == CATEGORY.get(self.category)]
        return sum(matching_die)
