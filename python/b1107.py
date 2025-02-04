while True:
  A, C = map(int, input().split());
  if A == 0 and C == 0: break;
  
  alt = list(map(int, input().split()));
  
  laser = A - alt[0];
  
  for i in range(C-1):
    if alt[i] > alt[i+1]:
      laser += alt[i] - alt[i+1];
  
  print(laser);