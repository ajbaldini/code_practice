"""
How do you find duplicate numbers in an array if it contains multiple duplicates?
"""

def find_all_dupes(numbers):
    checked_nums = []
    duplicates = []
    for i in numbers:
        if i not in checked_nums:
            checked_nums.append(i)
        else:
            duplicates.append(i)
    return duplicates

numbers = [1,2,3,4,5,6,7,5,8,9,7,10]
dupes = find_all_dupes(numbers)
print(str(dupes))