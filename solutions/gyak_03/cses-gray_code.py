# CSES - Gray Code
# https://cses.fi/problemset/task/2205

n = int(input().strip())

def gray_code(n):
    if n == 1:
        return ["0", "1"]
    prev = gray_code(n - 1)
    return ["0" + code for code in prev] + ["1" + code for code in reversed(prev)]

for code in gray_code(n):
    print(code)
