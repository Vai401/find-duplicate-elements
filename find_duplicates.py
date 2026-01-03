lst = [1, 2, 1, 3, 5, 4, 4]

seen = set()
duplicates = set()

for i in lst:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print("Duplicate elements:", list(duplicates))
 