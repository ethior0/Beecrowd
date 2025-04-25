while True:
  n = int(input());
  if n == 0: break;

  for i in range(1, n+1):
    res = "%3d" %i;
    flag = False;
    
    for j in range(n-1):
      if i > 1 and not(flag):
        i -= 1;
      elif i < 1:
        i += 1;
      else:
        i += 1;
        flag = True;
        
      res += " %3d" %i;
    
    print(res);
  print();
