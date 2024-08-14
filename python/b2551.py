while True:
  try:
    N = int(input());
    vM1 = 0;

    for i in range(N):
      T, D = map(int, input().split());
      vM2 = D / T;
      if vM2 > vM1:
        print(i+1);
        vM1 = vM2;

  except EOFError:
    break;