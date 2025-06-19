# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.add(10)          # Add an element to set1

set2.remove(6)        # Remove an element from set2

union_set = set1.union(set2)        # Find union of sets

intersection_set = set1.intersection(set2)      # Find intersection of sets

# Print the results
print("Set1:", set1)
print("Set2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
