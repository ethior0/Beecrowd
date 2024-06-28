def insertion_sort(lista):
  n = len(lista);
  for i in range(1, n):
    j = i;
    while j > 0 and len(lista[j]) > len(lista[j-1]):
      lista[j-1], lista[j] = lista[j], lista[j-1];
      j -= 1;

N = int(input())

for _ in range(N):
    lista = input().strip().split(' ')
    insertion_sort(lista)
    print(' '.join(lista))