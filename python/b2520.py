while True:
  try:
    N, M = map(int, input().split());

    X, Y = 0, 0; # eu
    aX, aY = 0, 0; # analogimon

    for i in range(N):
      linha = list(map(int, input().split()));
      for j in range(M):
        if linha[j] == 1: X, Y = i, j;
        elif linha[j] == 2: aX, aY = i, j;
    
    cc = 0;
    for k in range(N+M-1):
      if aX < X:
        X -= 1;
        cc += 1;
      elif aX > X:
        X += 1;
        cc += 1;
      if aY < Y: 
        Y -= 1;
        cc += 1;
      elif aY > Y: 
        Y += 1;
        cc += 1;
      if X == aX and Y == aY: break;
    print(cc);
  except EOFError:
    break;

# 2 -> 0, 0 (aX, aY)
# 1 -> 3, 2 (X, Y)

# se aX < X: X--
# senao se aX > X: X++
# senao se aY < Y: Y--
# senao se aY > Y: Y++
# se X == aX and Y == aY: break;
