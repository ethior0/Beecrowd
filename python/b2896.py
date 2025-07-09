t = int(input());

for _ in range(t):
  n, k = [int(x) for x in input().split()];
  print(n % k + n // k);