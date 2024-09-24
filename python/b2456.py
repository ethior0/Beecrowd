lista = list(map(int, input().split()));
crescente = sorted(lista);
decrescente = sorted(lista, reverse=True);

if lista == crescente:
  print("C");
elif lista == decrescente:
  print("D");
else:
  print("N");