from itertools import permutations
import numpy as np
import math

ints = np.array(range(1,11))

perms = permutations(ints)

hVals = []

for perm in perms:
    list1 = perm[5:]
    list2 = perm[:5]

    h = math.gcd(np.prod(list1),np.prod(list2))
    if h not in hVals:
        hVals.append(h)

print(hVals)
print(sum(hVals))
print(ints)
