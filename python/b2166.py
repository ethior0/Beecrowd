N = int(input());

res, denominador, aux = 1, 2, 2;
for i in range(N-1):
  if i == 0:
    denominador = ((aux * aux) + 1) / aux;
  else:
    denominador = ((aux * denominador) + 1) / denominador;

if N != 0:
  res += 1 / denominador;

print(f"{res:.10f}");