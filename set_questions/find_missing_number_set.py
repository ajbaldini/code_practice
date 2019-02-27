""" find the missing number in a given integer array of 1 to 100?
"""
import random

def build_set(numbers):
    for i in range(1,101):
        numbers.add(i)

def remove_random(numbers):
    removeNum = (random.randint(1,100))
    print("Removing: " + str(removeNum))
    numbers.remove(removeNum)
    return numbers

numbers = set()
build_set(numbers)
allnumbers = numbers.copy()
numbers = remove_random(numbers)

d = allnumbers.difference(numbers)

print ("missing number " + str(d))