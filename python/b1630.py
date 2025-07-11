import math;

while True:
  try:
    x, y = [int(x) for x in input().split()];
    if x == 0 and y == 0: break;
    
    aux = math.gcd(x, y);
    print((x // aux * 2) + (y // aux * 2));
  except EOFError:
    break;