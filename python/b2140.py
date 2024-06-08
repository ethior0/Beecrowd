bills = [2, 5, 10, 20, 50, 100];

while True:
  N, M = map(int, input().split());
  if N == 0 and M == 0: break;

  charge, cc1, bLen, res = M - N, 0, len(bills), "";

  while cc1 < bLen:
    numBill, cc2 = bills[cc1], 0;
    while cc2 < bLen:
      newNumBill = bills[cc2];
      if numBill + newNumBill == charge:
        res = "possible";
        break;
      cc2 += 1;
    if res == "possible": break;
    cc1 += 1;

  print(res) if res else print("impossible");