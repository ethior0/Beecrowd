import math;

T = int(input());

for i in range(T):
  conversao = input().strip();
  R, G, B = map(int, input().split());
  P = 0;
  
  if conversao == "eye":
    P = math.trunc((0.3 * R) + (0.59 * G) + (0.11 * B));
  elif conversao == "mean":
    P = (R + G + B) // 3;
  elif conversao == "max":
    P = max(R, G, B);
  else: # min
    P = min(R, G, B);
  
  print(f"Caso #{i+1}: {P}");