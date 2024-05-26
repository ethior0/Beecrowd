# TIME LIMIT EXCEEDED :|

import math;

N = int(input());
cc = 1;

while N != 0:
  totalX, totalY = 0, 0;
  array = {};
  
  for i in range(N):
    X, Y = map(int, input().split(" "));
    totalX += X;
    totalY += Y;
    if (Y//X in array):
      array[Y//X] += X;
    else: 
      array[Y//X] = X;
  
  consumo_total = math.floor((100 * totalY) / totalX) / 100;

  print(f"Cidade# {cc}:");

  output = [];
  keys = sorted(list(array.keys()));
  for key in keys:
    output.append(f"{array[key]}-{key}");
  
  print(f'{" ".join(output)}');
  print(f"Consumo medio: {consumo_total:.2f} m3.\n");

  cc += 1;
  N = int(input());