while True:
  m, n = [int(x) for x in input().split()];
  if m == 0 and n == 0: break;
  
  print(str(m+n).replace("0", ""));