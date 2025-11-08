"""
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union → {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection → {3, 4}
print(A - B)  # Difference → {1, 2}
print(A ^ B)  # Symmetric Difference → {1, 2, 5, 6}


Set Methods
add(x) → Adds item x to the set
remove(x) → Removes item x (error if not found)
discard(x) → Removes item x (no error if not found)
pop() → Removes and returns a random item
clear() → Removes all items
copy() → Returns a shallow copy


Union	Combines all unique elements from both sets	`A	BorA.union(B)`	{1, 2, 3, 4, 5, 6}
Intersection	Elements common to both sets	A & B or A.intersection(B)	{3, 4}
Difference	Elements in A but not in B	A - B or A.difference(B)	{1, 2}
Symmetric Difference	Elements in either A or B, but not both	A ^ B or A.symmetric_difference(B)	{1, 2, 5, 6}
Subset	Checks if A is a subset of B	A <= B or A.issubset(B)	True or False
Superset	Checks if A contains all elements of B	A >= B or A.issuperset(B)	True or False
Disjoint	Checks if sets have no elements in common	A.isdisjoint(B)	True or False
"""

import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0]=[9,9]
print(deep, shallow)