n, x = map(int, input().split());
titas = input();
p, m, g = input().split();

titas = " ".join(titas).replace("P", p).replace("M", m).replace("G", g);
titas = list(map(int, titas.split()));

muro = [x];
minMuro = [0] * (x + 1);
for i in range(n):
  titaAtual = titas[i];
  for j in range(minMuro[titaAtual], len(muro)):
    if muro[j] >= titaAtual:
      muro[j] -= titaAtual;
      break;
    if j == len(muro)-1:
      muro.append(x);
      muro[j+1] -= titaAtual;
  minMuro[titaAtual] = j;

print(len(muro));