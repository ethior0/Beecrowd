while True:
  try:
    string = str(input());
    N = int(input());
    lampadas = list(map(int, input().split()));

    msg = "";
    for i in lampadas:
      msg += string[i-1];
    print(msg);
  except EOFError:
    break;