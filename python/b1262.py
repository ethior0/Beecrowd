while True:
  try:
    texto = input();
    P = int(input());
    
    ciclos = 0;
    cc = 0;
    
    for i in range(len(texto)-1):
      if texto[i] == "W":
        ciclos += 1;
        cc = 0;
      elif texto[i] == "R":
        cc += 1;
        if texto[i+1] == "W" or cc == P:
          ciclos += 1;
          cc = 0;
    
    print(ciclos+1);
    
  except EOFError:
    break;