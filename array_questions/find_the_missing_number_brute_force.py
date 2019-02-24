""" find the missing number in a given integer array of 1 to 100?
"""
import random

def find_missing(numbers, lastNum):
    for i in range(1,lastNum+1):
        if i not in numbers:
            return i

def build_array(numbers):
    for i in range(1,101):
        numbers.append(i)

def remove_random(numbers):
    removeNum = (random.randint(1,100))
    print("Removing: " + str(removeNum))
    numbers.remove(removeNum)
    return numbers

numbers = []
build_array(numbers)
numbers = remove_random(numbers)

print ("missing number " + str(find_missing(numbers, 100)))

