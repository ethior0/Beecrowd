def selection_sort(lista):
  l = len(lista);
  for i in range(l-1):
    min_index = i;
    for j in range(i, l):
      if lista[j] < lista[min_index]:
        min_index = j;
    if lista[i] > lista[min_index]:
      lista[i], lista[min_index] = lista[min_index], lista[i];

lista = list([int(x) for x in input().split()]);
selection_sort(lista);

if lista[2] == lista[0] + lista[1] or lista[1] == lista[2] or lista[0] == lista[1]:
  print("S");
else:
  print("N");
