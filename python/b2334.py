while True:
  P = int(input());
  if P <= -1: break;

  print(0) if P <= 1 else print(P-1);