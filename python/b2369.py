N = int(input());
newN = N;

valor = 7;

if N >= 101:
  valor += (newN - 100) * 5;
  newN = 100;
if N >= 31:
  valor += (newN - 30) * 2;
  newN = 30;
if N >= 11:
  valor += (newN - 10);

print(valor);