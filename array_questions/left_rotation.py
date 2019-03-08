"""
Given an array  of  integers and a number, , perform  left rotations on the array.
Return the updated array to be printed as a single line of space-separated integers.
"""
def left_rotation(cnt,arr):
    for i in range(cnt):
        x = arr.pop(0)
        arr.append(x)

    return arr

print(left_rotation(4,[1,2,3,4,5]))
print(left_rotation(6,[1,2,3,4,5,6,7,8,9,10]))