# TIME LIMIT EXCEEDED :| 
# MAS EM JAVA FUNCIONA rsrsrs

import math;
cc = 1;

while True:
  N = int(input());
  if N == 0: break;

  array = [0] * 201;
  maiorIndice = 0;
  res = "";
  totalX, totalY = 0, 0;

  for _ in range(N):
    X, Y = map(int, input().split());
    totalX += X;
    totalY += Y;
    indice = Y // X;
    array[indice] += X;
    if indice > maiorIndice: 
      maiorIndice = indice;

  for i in range(0, maiorIndice+1):
    if array[i] != 0: 
      res = res + array[i] + "-" + i + " ";

  consumoM = int(totalY/totalX * 100)
  consumoM = consumoM/100

  print(f"Cidade# {cc}:");
  print(res.strip());
  print(f"Consumo medio: {consumoM:.2f} m3.\n");
  cc += 1;