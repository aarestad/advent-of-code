from fractions import Fraction
from typing import NamedTuple, List, Dict


class ReactionElement(NamedTuple):
    amount: int
    element: str

class OreRequirement(NamedTuple):
    ore_amt: int
    product_amt: int


class Reaction(NamedTuple):
    product: ReactionElement
    inputs: List[ReactionElement]


def requirements_for(element: str, existing_requirements: Dict[str, int]):
    try:
        for input in reactions[element].inputs:
            if input.element == 'ORE':
                break

            if input.element not in existing_requirements:
                existing_requirements[input.element] = input.amount
            else:
                existing_requirements[input.element] += input.amount

            existing_requirements = requirements_for(input.element, existing_requirements)
    except KeyError:
        pass

    return existing_requirements


if __name__ == '__main__':
    reactions = {}
    ore_requirements = {}

    with open('14_test_input.txt') as reaction_file:
        for reaction in reaction_file:
            inputs_str, product_str = reaction.strip().split(' => ')
            inputs = []

            for input_str in inputs_str.split(', '):
                split_amt = input_str.split(' ')
                inputs.append(ReactionElement(element=split_amt[1], amount=int(split_amt[0])))

            split_product = product_str.split(' ')
            product = ReactionElement(element=split_product[1], amount=int(split_product[0]))

            if len(inputs) == 1 and inputs[0].element == 'ORE':
                ore_requirements[product.element] = OreRequirement(inputs[0].amount, product.amount)
            else:
                reactions[product.element] = Reaction(product, inputs)

    requirements = requirements_for('FUEL', {})
    print(requirements)
    print(ore_requirements)

    total_ore = 0

    for element in requirements.keys():
        try:
            ore_requirement = ore_requirements[element]
            amt_required = requirements[element]
            multiplier = (amt_required // ore_requirement.product_amt)

            if amt_required % ore_requirement.product_amt != 0:
                multiplier += 1

            more_ore = multiplier * ore_requirement.ore_amt
            print('{} more ore for {}'.format(more_ore, element))
            total_ore += more_ore

        except KeyError:
            pass

    print(total_ore)
