  # 3 3
  # [0, 0, 0]
  # [1, 1, 1]
  # [1, 2, 2]
  # [2, 3, 3]

while True:
  n, d = [int(x) for x in input().split()];
  if n == d == 0: break;
  
  arr = [0 for _ in range(n)];
  
  for _ in range(d):
    for i, c in enumerate([int(x) for x in input().split()]):
      if c: arr[i] += 1;
  
  res = "no";
  for j in range(n):
    if arr[j] == d:
      res = "yes";
      break;
  
  print(res);