N = int(input());
sqr = [];

for _ in range(N):
  sqr.append(list(map(int, input().split())));

M = sorted([sum(sqr[0]), sum(sqr[1]), sum(sqr[2])])[1];

linha, coluna = 0, 0;

# checa as linhas
for i in range(N):
  if sum(sqr[i]) != M:
    linha = i;

# checa as colunas
for j in range(N):
  soma = 0;
  for k in range(N):
    soma += sqr[k][j];
  if soma != M:
    coluna = j;


alterado = sqr[linha][coluna];
original = alterado - (sum(sqr[linha]) - M);

print(original, alterado);