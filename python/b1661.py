n = int(input());

while n != 0:
  val = list(map(int, input().split()));
  res, aux = 0, 0;
  
  for a in val:
    aux += a;
    res += abs(aux);
  
  print(res);
  n = int(input());