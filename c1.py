l = [x+y for x in [10,20] for y in [5]]
print(l) # [15, 25]

l1 = []
for i in [10,20]:
    for j in [5]:
        l1.append(i+j)
print(l1)     # [15, 25]   