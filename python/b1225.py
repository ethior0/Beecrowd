while True:
  try:
    n = int(input());
    a = [int(x) for x in input().split()];

    soma = sum(a);
    
    if soma % n != 0:
      print(-1);
    else:
      res = 0;
      for i in range(n):
        if a[i] > soma // n:
          res += a[i] - (soma // n);
      print(res+1);

  except EOFError:
    break;