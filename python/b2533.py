while True:
  try:
    M = int(input());
    somatorio1 = 0;
    somatorio2 = 0;

    for _ in range(M):
      N, C = map(int, input().split());
      somatorio1 += N * C;
      somatorio2 += C;
    ira = somatorio1 / (somatorio2 * 100);
    print(f"{ira:.4f}");
  except EOFError:
    break;