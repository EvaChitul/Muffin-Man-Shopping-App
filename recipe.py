

class Recipe:
    is_initialized = False

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients if ingredients else {}

    def __str__(self):
        number_of_stars = len(self.name) + 3
        pretty_string = '*' * number_of_stars + '\n' + self.name + '\n' + '*' * number_of_stars + '\n'

        for index, (key, value) in enumerate(self.ingredients.items(), start=1):
            pretty_string = '\n'.join((pretty_string, f'{index}. {key.title()}: {value}'))

        pretty_string = pretty_string + '\n' * 2 + '*' * number_of_stars
        return pretty_string

    def __getitem__(self, given_index):
        for index, (key, value) in enumerate(self.ingredients.items(), start=1):
            if given_index == index:
                return {key: value}

    def __len__(self):
        return len(self.ingredients)

    def __iter__(self):
        return iter(self.ingredients)

    def keys(self):
        return self.ingredients.keys()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self.is_initialized:
            raise NameError("You can't update the recipe!")
        self._name = name

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if self.is_initialized:
            raise NameError("You can't update the recipe!")
        self._ingredients = ingredients
        self.is_initialized = True