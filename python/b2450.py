N, M = map(int, input().split());
matriz, res, linhaZero, ccK = [], "", False, 0;

for i in range(N):
  listaNum = list(map(int, input().split()));
  matriz.append(listaNum);

for j in range(N):
  ccZero = 0;
  for k in range(M):
    if j > 0 and k < ccK:
      if matriz[j][k] == 0: 
        res = "S";
      else:
        res = "N";
        break;
    if matriz[j][k] != 0 and linhaZero == False:
      ccK = k+1;
      break;
    else: 
      ccZero += 1;
    if ccZero == M:
      linhaZero = True;
      ccK = M;
  if res == "N": break;

print(res);