n = int(input());

for _ in range(n):
  t = int(input());
  a = [int(x) for x in input().split()];
  b = input();

  res = 0;
  for i, valor in enumerate(a):
    if (b[i] == "J" and valor > 2) or (b[i] == "S" and (valor == 1 or valor == 2)):
      res += 1;
  
  print(res);