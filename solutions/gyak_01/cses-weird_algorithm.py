# CSES - Weird Algorithm
# https://cses.fi/problemset/task/1068/

num = int(input())
print(num, end=' ')

while num > 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    print(num, end=' ')
