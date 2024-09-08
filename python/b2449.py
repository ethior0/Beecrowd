N, M = map(int, input().split());
lista = list(map(int, input().split()));
minMovs = 0;

if N >= 2:
  pinoInicial = M - lista[0];
  lista[0] += pinoInicial;
  lista[0+1] += pinoInicial;
  minMovs += abs(pinoInicial);
if N >= 3:
  pinoFinal = M - lista[N-1];
  lista[N-1] += pinoFinal;
  lista[N-2] += pinoFinal;
  minMovs += abs(pinoFinal);

for i in range(1, N-1):
  if lista[i] != M:
    soma = M - lista[i];
    lista[i] += soma;
    lista[i+1] += soma;
    minMovs += abs(soma);

print(minMovs);

# 84 39 17 72 94
# 84 39 17 [62 84] -> + 10
# 84 [84 62] 62 84 -> + 45
# 84 84 [84 84] 84 -> + 22
# 84 84 84 84 84 -> 77