N = int(input());
lista = [0] * 2001;

for _ in range(N):
  X = int(input());
  lista[X] += 1;

for i in range(len(lista)):
  if lista[i] > 0:
    print(f"{i} aparece {lista[i]} vez(es)");