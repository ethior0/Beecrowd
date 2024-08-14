while True:
  try:
    N, Amin, Amax = map(int, input().split());
    cc = 0;

    for _ in range(N):
      A = int(input());
      if A >= Amin and A <= Amax: cc += 1;
  
    print(cc);
  except EOFError:
    break;