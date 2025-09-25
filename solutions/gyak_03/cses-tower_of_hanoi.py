# CSES - Tower of Hanoi
# https://cses.fi/problemset/task/2165/

n = int(input().strip())
count_steps = 0
move_list = []

def tower_of_hanoi(n, source, target, helper):

    global count_steps

    if n == 1:
        move_list.append(f"{source} {target}")
        count_steps += 1
        return

    # Move n-1 disks from source to helper
    tower_of_hanoi(n-1, source, helper, target)

    # Move the largest disk from source to target
    move_list.append(f"{source} {target}")
    count_steps += 1

    # Move n-1 disks from helper to target
    tower_of_hanoi(n-1, helper, target, source)

tower_of_hanoi(n, 1, 3, 2)
print(count_steps)
[print(move) for move in move_list]
