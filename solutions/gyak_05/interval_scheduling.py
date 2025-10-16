# Activity Selection (Interval Scheduling)
# Task: Given start and end times of activities, select the maximum number of non-overlapping ones.

def activity_selection(activities):
    # Sort by finishing time
    activities.sort(key=lambda x: x[1])

    selected = []
    last_end = -float('inf')

    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


# Example
activities = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7), (8, 9)]
chosen = activity_selection(activities)

print("All activities (start, end):", activities)
print("\nSelected activities:")
for s, e in chosen:
    print(f"({s}, {e})")
