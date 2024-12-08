limite = [0 for _ in range(100001)];

N = int(input());
fila = [int(x) for x in input().split()];
for f in fila:
  limite[f] += 1;

M = int(input());
sairam = [int(y) for y in input().split()];
for s in sairam:
  limite[s] -= 1;

res = "";
maiorIndex = max(fila);
for num in fila:
  if limite[num] == 1:
    res += f"{num} ";

print(res.strip());