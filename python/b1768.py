while True:
  try:
    n = int(input());
    
    a = "*";
    for i in range(n // 2 + 1):
      print(f"{a:>{n // 2 + 1 + i}}");
      a += "**";
    
    print(f"{'*':>{n // 2 + 1}}");
    print(f"{'***':>{n // 2 + 2}}");
    print();
  except EOFError:
    break;