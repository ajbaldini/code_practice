def sumofints(n):
    if n == 1:
        return 1
    else:
        return sumofints(n-1)+n

print(sumofints(4))