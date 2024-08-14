while True:
  try:
    N, I = map(int, input().split());
    cc = 0;

    for _ in range(N):
      i, j = map(int, input().split());
      if i == I and j == 0: cc += 1;
    
    print(cc);
  except EOFError:
    break;