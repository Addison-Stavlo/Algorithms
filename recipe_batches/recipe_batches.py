#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    amount_can_make = 0
    canMake = True
    while canMake:
        for items in recipe:
            if items in ingredients:
                if recipe[items] <= ingredients[items]:
                    ingredients[items] -= recipe[items]
                else:
                    canMake = False
            else:
                canMake = False
        if(canMake):
            amount_can_make += 1
    return amount_can_make


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

stuff = {'milk': 100, 'butter': 50, 'flour': 5}
for each in stuff:
    print(each, stuff[each])
