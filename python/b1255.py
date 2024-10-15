alfabeto = "abcdefghijklmnopqrstuvwxyz";
N = int(input());

for _ in range(N):
  texto = input().lower();
  
  ccMaior = 0;
  res = "";
  
  for letra in alfabeto:
    ccLetra = texto.count(letra);
    if ccLetra > ccMaior:
      ccMaior = ccLetra;
      res = letra;
    elif ccLetra == ccMaior:
      res += letra;
  
  print(res);