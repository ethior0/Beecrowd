T = int(input());

for _ in range(T):
  B = int(input());
  A1, D1, L1 = [int(x) for x in input().split()];
  A2, D2, L2 = [int(x) for x in input().split()];
  vGolpe1 = (A1 + D1) / 2;
  vGolpe2 = (A2 + D2) / 2;

  if L1 % 2 == 0:
    vGolpe1 += B;
  if L2 % 2 == 0:
    vGolpe2 += B;

  if vGolpe1 == vGolpe2:
    print("Empate");
  elif vGolpe1 > vGolpe2:
    print("Dabriel");
  else:
    print("Guarte");