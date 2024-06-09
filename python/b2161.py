N = int(input());

res, denominador = 3, 6;
for i in range(N-1):
  if i == 0:
    denominador = ((6 * 6) + 1) / 6;
  else:
    denominador = ((6 * denominador) + 1) / denominador;

if N >= 1: res += 1 / denominador;
print(f"{res:.10f}");