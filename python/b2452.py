F, R = map(int, input().split());
gotas = list(map(int, input().split()));
fita = [0 for _ in range(F)];

dia, aux, infectados = 0, 1, R;

for num in gotas:
  fita[num-1] = 1;

for i in range(F):
  for j in gotas:
    if j+aux-1 < F and fita[j+aux-1] == 0:
      fita[j+aux-1] = 1;
      infectados += 1;
    if j-aux-1 >= 0 and fita[j-aux-1] == 0:
      fita[j-aux-1] = 1;
      infectados += 1;
  aux += 1;
  dia += 1;
  if infectados == F: break;

print(dia);