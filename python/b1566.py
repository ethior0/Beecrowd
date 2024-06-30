def counting_sort(lista, maior):
  maior = maior + 1;
  cc = [0] * maior;
  for i in lista:
    cc[i] += 1;
  j = 0;
  for i in range(maior):
    for k in range(cc[i]):
      lista[j] = i;
      j += 1;
  return lista;

nc = int(input());

for _ in range(nc):
  n = int(input());
  listaH = list(map(int, input().split()));
  counting_sort(listaH, max(listaH));
  print(" ".join(str(x) for x in listaH));
