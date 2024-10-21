while True:
  try:
    num = str(float(input()));
    cutoff = str(float(input()));
    
    numF = num[num.index(".")+1:len(num)];
    cutoffF = cutoff[cutoff.index(".")+1:len(cutoff)];
    res = int(float(num));
    
    if numF > cutoffF:
      res += 1;
    
    print(res);
  except EOFError:
    break;