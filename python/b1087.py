while True:
  x1, y1, x2, y2 = map(int, input().split());
  
  if not x1: break;
  
  if x1 == x2 and y1 == y2:
    print(0);
  elif x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
    print(1);
  else:
    print(2);