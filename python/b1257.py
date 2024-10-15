alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
N = int(input());

for i in range(N):
  L = int(input());
  res = 0;
  
  for j in range(L):
    texto = input();
    
    for k in range(len(texto)):
      res += alfabeto.index(texto[k]) + j + k;
  
  print(res);