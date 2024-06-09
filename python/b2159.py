import math;

n = int(input());
P = n / math.log(n);
M = 1.25506 * P;

print(f"{P:.1f} {M:.1f}");