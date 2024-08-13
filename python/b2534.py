while True:
  try:
    N, Q = map(int, input().split());
    arr = [];

    for _ in range(N):
      n = int(input());
      arr.append(n);
    
    arr.sort(reverse=True);

    for _ in range(Q):
      p = int(input());
      print(arr[p-1]);
  except EOFError:
    break;