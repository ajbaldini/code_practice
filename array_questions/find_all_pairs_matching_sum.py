"""
How do you find all pairs of an integer array whose sum is equal to a given number?
"""

def find_pairs(numbers, sum):

    for i in numbers:
        for x in numbers:
            if i + x == sum:
                print (f"{i} and {x} equal {sum}")

numbers = [1,2,3,4,5,6,7,8,9,10]
find_pairs(numbers, 13)