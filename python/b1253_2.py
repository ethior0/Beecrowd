N = int(input());
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

for _ in range(N):
  palavra = input();
  desloc = int(input());
  res = "";
  
  for letra in palavra:
    indexLetra = alfabeto.find(letra);
    res += alfabeto[(indexLetra - desloc) % 26];
  print(res);