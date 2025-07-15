while True:
  n = int(input());
  if n == 0: break;
  
  pos = [0] * n;
  
  flag = True;
  for i in range(n):
    c, p = map(int, input().split());
    
    aux = 0;
    if p == 0:
      aux = i;
    else:
      aux = i+p;
    
    if aux < 0 or aux >= n:
      flag = False;
      continue;
    if pos[aux] != 0:
      flag = False;

    pos[aux] = c;
  
  if flag:
    print(*pos);
  else:
    print(-1);