N = int(input());
array = [];

for _ in range(N+1):
  array.append(list(map(int, input().split())));

for i in range(N):
  res, cc = "", 0;
  for j in range(N):
    if array[i][j] == 1: cc += 1;
    if array[i][j+1] == 1: cc += 1;
    if array[i+1][j] == 1: cc += 1;
    if array[i+1][j+1] == 1: cc += 1;
    
    if cc >= 2: 
      res += "S";
    else: 
      res += "U";
    cc = 0;
  print(res);
