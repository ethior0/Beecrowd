import math;

N = int(input());
numbers = [100, 50, 20, 10, 5, 2, 1];

print(N);
for i in numbers:
  print(f"{math.trunc(N / i)} nota(s) de R$ {i},00");
  N = N % i;