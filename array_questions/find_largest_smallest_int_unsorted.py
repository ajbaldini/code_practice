
def large_and_small(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i;
        elif i < smallest:
            smallest = i
    return(smallest, largest)


numbers = [3,27,87,4,30,43,200, -54, 2000]
small, large = large_and_small(numbers)
print("Largest " + str(large) + " Smallest " + str(small))