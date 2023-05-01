# Define two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Perform set operations
union = set_a.union(set_b)
intersection = set_a.intersection(set_b)
difference = set_a.difference(set_b)
symmetric_difference = set_a.symmetric_difference(set_b)

# Print the results
print("Set A: ", set_a)
print("Set B: ", set_b)
print("Union: ", union)
print("Intersection: ", intersection)
print("Difference (A-B): ", difference)
print("Symmetric Difference: ", symmetric_difference)
