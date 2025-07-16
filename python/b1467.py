while True:
  try:
    a, b, c = map(int, input().split());
    
    if a == b and b == c:
      print("*");
    elif a == b:
      print("C");
    elif b == c:
      print("A");
    elif a == c:
      print("B");
  except EOFError:
    break;