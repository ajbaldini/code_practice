""""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements. You need to find the minimum number of swaps required to
sort the array in ascending order

TODO Times out at 50000 records
"""

def minimumSwaps(arr):
    curr_index = 1
    swap = 0

    for i in range(len(arr)-1):
        if arr[i] != curr_index:

            print(range(len(arr)-1))
            for j in range(len(arr)-1):
                x = arr[j]
                if x == curr_index:
                    arr[i], arr[j] = arr[j], arr[i]
                    swap += 1
                    break
        curr_index += 1
    return swap

print(minimumSwaps([1,3,2,5,4])) #2
print(minimumSwaps([4,3,1,2])) #3
print(minimumSwaps([1,3,5,2,4,6,7]))