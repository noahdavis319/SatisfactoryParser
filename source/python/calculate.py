
import os
import sys
import json
import math
from fractions import Fraction


def calc():
    if not os.path.exists('../resources/components.json'):
        print('components JSON file missing from resources!\n\tRun main.py to generate it.')
        sys.exit(1)

    comp = None
    with open('../resources/components.json', 'r') as f:
        comp = json.loads(f.read())

    if comp is None:
        print('Error loading JSON data from components file.')
        sys.exit(1)

    item = input('Item name: ')

    if item not in comp:
        print('Could not find item in component list. Check spelling, punctuation, and capitalization.')
        sys.exit(1)

    calc_item(item, comp)


def calc_item(item, data):
    for ingredient in data[item]['ingredients']:
        i = data[item]['ingredients'][ingredient]
        needed_total = float(i['rate'])
        num_parent_machines = calc_num_machines(i, ingredient, data, needed_total)
        print('{0} w/ {1}: {2:.3f} [{3}] ({4})'.format(ingredient, get_ingredient_machine(ingredient, data),
                                                       num_parent_machines,
                                                       str(dec_to_proper_frac(num_parent_machines)),
                                                       math.ceil(num_parent_machines)))

    for ingredient in data[item]['ingredients']:
        if 'Ore' not in ingredient:
            calc_item(ingredient, data)


def dec_to_proper_frac(dec):
    sign = "-" if dec < 0 else ""
    frac = Fraction(abs(dec)).limit_denominator()
    return (f"{sign}{frac.numerator // frac.denominator} "
            f"{frac.numerator % frac.denominator}/{frac.denominator}")


def calc_num_machines(i, name, data, total):
    item = data[name]
    building = item['building']
    time = int(building['time'].split(' ')[0])
    max_per_min = 60 / time
    return total / max_per_min


def get_ingredient_machine(name, data):
    return data[name]['building']['type']


if __name__ == '__main__':
    calc()
