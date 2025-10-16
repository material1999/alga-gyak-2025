# Fractional Knapsack Problem
# Task: Items have weights and values; you can take fractions of items. Maximize total value for a weight limit.

def fractional_knapsack(items, capacity):
    # items = list of (value, weight)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    fractions = []
    remaining_capacity = capacity

    for value, weight in items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            # take whole item
            fractions.append((value, weight, 1.0))
            total_value += value
            remaining_capacity -= weight
        else:
            # take fraction of item
            fraction = remaining_capacity / weight
            fractions.append((value, weight, fraction))
            total_value += value * fraction
            remaining_capacity = 0

    return total_value, fractions


# Example
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50

max_value, taken = fractional_knapsack(items, capacity)

print(f"Knapsack capacity: {capacity}")
print("\nItems taken (value, weight, fraction):")
for v, w, f in taken:
    print(f"({v}, {w}) → {f * 100:.1f}%")
print(f"\nTotal value = {max_value:.2f}")
