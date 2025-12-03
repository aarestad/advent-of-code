import re


class Ingredient(object):
    _parser = re.compile(
        r"(.+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
    )

    def __init__(self, s):
        match = Ingredient._parser.match(s)
        self.name = match.group(1)
        self.capacity = match.group(2)
        self.durability = match.group(3)
        self.flavor = match.group(4)
        self.texture = match.group(5)
        self.calories = match.group(6)

    def __str__(self):
        return "Ingredient: " + self.__dict__.__str__()


with open("input_15.txt") as ingredients:
    for i in ingredients:
        print(Ingredient(i))
