import math
max = 0
for i in range(6000,9000):
    a = i/100
    k = math.sqrt(2*a / (math.sin(a*math.pi/180)))
    b = 2*k*math.sin(a*math.pi/360)
    
    r = (b/2) * math.sqrt((2*k-b)/(2*k+b))

    a_2 = 180 - 2*i/100
    k_2 = math.sqrt(2*a_2 / math.sin(a_2*math.pi/180))
    b_2 = 2*k_2*math.sin(a_2*math.pi/360)

    R = (b_2/2) * math.sqrt((2*k_2-b_2)/(2*k_2+b_2))
    
    A = math.pi * r**2 + math.pi * R**2
    if A > max:
        max = A

    print(A)

print(max)