import math;

N = int(input());

for _ in range(N):
  F1, F2 = map(int, input().split());
  print(math.gcd(F1, F2)); # Pog