
def find_duplicate(numbers):
    nums_checked = []
    duplicates = []
    for i in numbers:
        if i not in nums_checked:
            nums_checked.append(i)
        else:
            duplicates.append(i)
    return duplicates


numbers = [1,2,3,2,4,5,1,6]
dupes = find_duplicate(numbers)
print("duplicates " + str(dupes))