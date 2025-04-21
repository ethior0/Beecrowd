while True:
  n, m = [int(x) for x in input().split()];
  if n == m == 0: break;
  arr = [int(x) for x in input().split()];
  
  b = [0 for _ in range(n+1)];
  
  res = 0;
  for i in arr:
    b[i] += 1;
    if b[i] == 2:
      res += 1;
  
  print(res);