N = int(input());

for _ in range(N):
  nome = input();
  gd = float(input());
  notas = list(map(float, input().split()));

  maiorNota = max(notas);
  menorNota = min(notas);

  res = (sum(notas) - maiorNota - menorNota) * gd;
  print(f"{nome} {res:.2f}");