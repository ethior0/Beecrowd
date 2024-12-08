# Algoritmo de Kadane

N = int(input());
lista = list(map(int, input().split()));

somaAtual = 0;
maiorSoma = lista[0];

for i in range(0, N):
  num = lista[i];
  if somaAtual + num > num:
    somaAtual += num;
  else:
    somaAtual = num;
  maiorSoma = max(maiorSoma, somaAtual);

print(maiorSoma);