import math

max = 0


for a in range(1,99):
    for b in range(1,99):
        for c in range(1,99):
            for d in range(1,99):
                m = (math.sqrt(a)+math.sqrt(b))*(math.sqrt(c)-math.sqrt(d))
                if int(m) == m and m > max and len(set([a,b,c,d])) == 4:
                    max = m
                    print(a,b,c,d)
            
print(max)