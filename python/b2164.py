import math;

n = int(input());
sqrtFive = math.sqrt(5);
aux1 = math.pow(((1 + sqrtFive) / 2), n);
aux2 = math.pow(((1 - sqrtFive) / 2), n);
res = (aux1 - aux2) / sqrtFive;

print(f"{res:.1f}");