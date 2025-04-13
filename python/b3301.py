H, Z, L = map(int, input().split());
lista = [H, Z, L];
lista.sort();

if lista[1] == H:
  print("huguinho");
elif lista[1] == Z:
  print("zezinho");
else:
  print("luisinho");
