n = int(input());
a, l, p = map(int, input().split());

if a >= n and l >= n and p >= n:
  print("S");
else:
  print("N");