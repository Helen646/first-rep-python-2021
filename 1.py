def func(num):
    num = num%2
    if num == 0:
        return ("Yes")
    elif num != 0:
        return ("No")
    else:
        return func(num)
num = int(input())

print(func(num))


