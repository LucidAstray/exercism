class Allergies2:

    def __init__(self, score):
        self.score = score
        self.allergens = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

    def is_allergic_to(self, item):

        hmm = list(bin(self.score)[2:])
        hmm.reverse()
        self.allergens = self.allergens[:len(hmm)]
        check = dict(zip(self.allergens, hmm))

        if item in check and check[item] == '1':
            return True
        else:
            return False

    @property
    def lst(self):
        return [a for a in self.allergens if self.is_allergic_to(a) and len(a) != 0]


'''Other take on allergies, shorter is_allergic, using Bitwise Operators:'''


class Allergies:

    def __init__(self, score):
        self.allergens = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
        check = lambda a: score & 2**(self.allergens.index(a))
        self.allergic_to = [allerg for allerg in self.allergens if check(allerg)]

    def is_allergic_to(self, allergen):
        return allergen in self.allergic_to

    @property
    def lst(self):
        return self.allergic_to
