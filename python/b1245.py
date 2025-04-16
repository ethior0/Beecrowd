while True:
  try:
    n = int(input());
    
    arrE = [0 for _ in range(61)];
    arrD = [0 for _ in range(61)];
    
    res = 0;
    for _ in range(n):
      m, l = input().split();
      m = int(m);
      
      if l == "E":
        arrE[m] += 1;
      else:
        arrD[m] += 1;
      
      if arrE[m] and arrD[m]:
        arrE[m] -= 1;
        arrD[m] -= 1;
        res += 1;
    
    print(res);
    
  except EOFError:
    break;