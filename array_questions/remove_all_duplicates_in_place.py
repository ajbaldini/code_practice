def remove_dupes(numbers):
    numCopy = numbers.copy()
    x = 0
    checked_nums = []
    for i in numCopy:
        if i in checked_nums:
            numCopy.pop(x)
        checked_nums.append(i)
        x = x + 1
    return numCopy

numbers = [1,2,3,4,5,6,2,7,8,4,9,]
noDupes = remove_dupes(numbers)
print("Original " + str(numbers) + " Cleaned " + str(noDupes))