N = float(input());
notes = [100, 50, 20, 10, 5, 2];
coins = [100, 50, 25, 10, 5, 1];

print("NOTAS:");
for i in notes:
  print(f"{int(N / i)} nota(s) de R$ {i}.00");
  N = N % i;

N *= 100;

print("MOEDAS:");
for j in coins:
  print(f"{int(N / j)} moeda(s) de R$ {(j/100):.2f}");
  N = N % j;