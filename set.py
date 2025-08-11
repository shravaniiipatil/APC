a = {1, 2, 3, 4}
print("Set a:", a)

b = set([5, 6, 7, 8])
print("Set b:", b)

a.add(5)
print("After adding 5 to a:", a)

b.remove(5) 
print("After removing 5 from b:", b)

b.update([1, 2, 3])
print("After updating b with [1, 2, 3]:", b)

print("Intersection of a and b:", a & b)

print("Union of a and b:", a|b)

print("Difference a - b:", a-b)

print("Symmetric Difference:", a^b)
