"""
Find the min sum and max sum of an array of integers
"""

def miniMaxSum(arr):
    arr.sort()

    min = arr[0:len(arr) - 1]
    max = arr[1:len(arr)]

    print(sum(min), sum(max))

a = [7,69,2,221,8974]
miniMaxSum(a)