def busca_binaria(lista, valor):
  primeiro = 0;
  ultimo = len(lista) - 1;
  meio = 0;
  while primeiro <= ultimo:
    meio = (ultimo + primeiro) // 2;
    if lista[meio] < valor:
      primeiro = meio + 1;
    elif lista[meio] > valor:
      ultimo = meio - 1;
    else: return meio;

N, M = map(int, input().split());
listaN = list(map(int, input().split()));
listaM = list(map(int, input().split()));
atual, tempo = 0, 0;

for carta in listaM:
  casaIndex = busca_binaria(listaN, carta);
  tempo += abs(casaIndex - atual);
  atual = casaIndex;

print(tempo);