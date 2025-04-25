arr = [True for _ in range(5001)];

for i in range(1, 5001):
  aux = str(i);
  for j in aux:
    if aux.count(j) > 1:
      arr[i] = False;
      continue; 

while True:
  try:
    n, m = map(int, input().split());
    
    res = 0;
    for i in range(n, m+1):
      if arr[i]: res += 1;
    
    print(res);
  except EOFError:
    break;