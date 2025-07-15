# a, b
# m = min(a, b)
# m = (a + b + c) / 3
# 3m - (a + b) = c

while True:
  a, b = map(int, input().split());
  if a == 0 and b == 0: break;
  
  s = a + b;
  m = min(a, b);
  c = 3 * m - (a + b);
  
  print(c);