#Dice Roller

import random

num_rolls = int(input("Enter the number of rolls: "))
num_sides = int(input("Enter the number of sides on the die: "))


def roll_dice(num_rolls, num_sides):
    results = []
    for i in range(num_rolls):
        roll = random.randint(1, num_sides)
        results.append(roll)
    print(results)

roll_dice(int(input("Enter number of rolls")), int(input("Enter number of sides on the die: ")))