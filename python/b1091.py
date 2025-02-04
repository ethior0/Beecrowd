while True:
  k = int(input());
  if k == 0: break;
  
  n, m = map(int, input().split());

  for _ in range(k):
    x, y = map(int, input().split());
    
    if n == x or m == y:
      print("divisa");
    elif x < n and y > m:
      print("NO");
    elif x > n and y > m:
      print("NE");
    elif x < n and y < m:
      print("SO");
    else:
      print("SE");