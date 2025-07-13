# FALTA COMPLETAR ESSE

while True:
  n = int(input());
  if n == 0: break;
  
  res = 0;
  for _ in range(n):
    c, v = map(int, input().split());
    if v % 2 != 0:
      v -= 1;
    res += v;
  
  print(res // 4);