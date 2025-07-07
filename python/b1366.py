# FALTA COMPLETAR ESSE

while True:
  n = int(input());
  if n == 0: break;
  
  arr = [];
  
  res = 0;
  for _ in range(n):
    c, v = map(int, input().split());
    if v >= 2:
      arr.append([c, v]);

  
  print(arr);
  print(res);