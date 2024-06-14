import math;

while True:
  try:
    Xf, Yf, Xi, Yi, Vi, R1, R2 = map(int, input().split());
    dis = math.sqrt(pow((Xi - Xf), 2) + pow((Yi - Yf), 2));

    if R1 + R2 >= dis + 1.5 * Vi:
      print("Y");
    else:
      print("N");

  except EOFError: break;