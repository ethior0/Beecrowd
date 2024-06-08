while True:
  T = int(input());
  if T == 0: break;

  for _ in range(T):
    num = int(input());
    if num % 2 == 0:
      print(num * 2 - 2);
    else:
      print(num * 2 - 1);