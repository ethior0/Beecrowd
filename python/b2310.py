N = int(input());
totalArr = [0, 0, 0];
acertosArr = [0, 0, 0];

for _ in range(N):
  nome = input();
  total = list(map(int, input().split()));
  acertos = list(map(int, input().split()));

  for i in range(len(total)):
    totalArr[i] += total[i];
    acertosArr[i] += acertos[i];

print(f"Pontos de Saque: {(acertosArr[0] / totalArr[0] * 100):.2f} %.");
print(f"Pontos de Bloqueio: {(acertosArr[1] / totalArr[1] * 100):.2f} %.");
print(f"Pontos de Ataque: {(acertosArr[2] / totalArr[2] * 100):.2f} %.");
