# Accumulating values into a dict by key
# Drill 1
scores = [("Alice", 10), ("Bob", 5), ("Alice", 7), ("Charlie", 3), ("Bob", 2)]
total_scores = {}
for a in scores:
    total_scores[a[0]] = total_scores.get(a[0], 0) + int(a[1])
print(total_scores)

# Drill 2
animals = [{"type": "cat"}, {"type": "dog"}, {"type": "cat"}, {"type": "cat"}, {"type": "dog"}]
total = {}
for b in animals:
    total[b["type"]] = total.get(b["type"], 0) + 1
print(total)

# Drill 3
orders = [("apple", 4), ("banana", 2), ("apple", 1), ("apple", 3), ("banana", 5)]
total_quantity = {}
for c in orders:
    total_quantity[c[0]] = total_quantity.get(c[0], 0) + int(c[1])
for item, quantity in total_quantity.items():
    print(f"{item}: {quantity}")