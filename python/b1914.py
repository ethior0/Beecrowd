QT = int(input());

for i in range(QT):
  p1, ch1, p2, ch2 = input().split();
  N, M = map(int, input().split());
  if (N + M) % 2 == 0:
    print(p1) if ch1 == "PAR" else print(p2);
  else:
    print(p1) if ch1 == "IMPAR" else print(p2);