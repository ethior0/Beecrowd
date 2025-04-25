while True:
  s = input().split();
  if s[0] == "*": break;
  
  ehTautograma = True;
  for i in range(len(s)-1):
    atual = s[i].lower();
    prox = s[i+1].lower();
    
    if atual[0] != prox[0]:
      ehTautograma = False;
      break;
  
  print("Y" if ehTautograma else "N");