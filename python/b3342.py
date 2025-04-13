n = int(input());
tab = n * n;
b, p = 0, 0;

if n % 2 == 0:
  b = tab // 2;
  p = tab // 2;
else:
  b = (tab - 1) // 2 + 1;
  p = (tab - 1) // 2

print(f"{b} casas brancas e {p} casas pretas")