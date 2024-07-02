def counting_sort(lista, maior):
  cc = [0] * maior + 1;
  k = 0;

  for i in lista:
    cc[i] += 1;

  for i in range(maior + 1):
    for j in range(cc[i]):
      lista[k] = i;
      k += 1;

nc = int(input());

for _ in range(nc):
  n = int(input());
  listaH = list(map(int, input().split()));
  counting_sort(listaH, max(listaH));
  print(" ".join(str(x) for x in listaH));
