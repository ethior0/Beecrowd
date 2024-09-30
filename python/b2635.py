palavras = [];

N = int(input());
for _ in range(N):
  palavras.append(input());

Q = int(input());
for _ in range(Q):
  consulta = input();
  lenP, ccP = 0, 0;
  for palavra in palavras:
    if palavra.find(consulta, 0, len(consulta)) != -1:
      if len(palavra) > lenP:
        lenP = len(palavra);
      ccP += 1;
  print(ccP, lenP) if ccP > 0 else print(-1);