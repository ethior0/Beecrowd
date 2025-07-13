while True:
  try:
    n = int(input());
    if n == 0: break;
    
    c, d = 0, 0;
    for _ in range(n):
      a, b = map(int, input().split());
      if a > b: c += 1;
      if b > a: d += 1;
    
    print(c, d);
  except EOFError:
    break;