nc = int(input());

for i in range(nc):
  n, k = map(int, input().split());

  circulo = list(range(1, n+1));
  
  salto = 1;
  ind = 0;

  while len(circulo) > 1:
    if ind >= len(circulo):
      ind = 0;
    num = circulo[ind];
    if salto == k:
      circulo.remove(num);
      salto = 1;
      continue;
    ind += 1;
    salto += 1;

  print(f"Case {i+1}: {circulo[0]}");