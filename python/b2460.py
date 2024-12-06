# 10 9 6 3
# 1 1 1 1
# 1 1 1 0
# 10 9 6

N = int(input());
fila = input().split();
filaSet = set(map(int, fila));

M = int(input());
sairam = input().split();
sairamSet = set(map(int, sairam));

filaSet.difference_update(sairamSet);

res = "";
for i in range(N):
  num = int(fila[i]);
  if num in filaSet:
    res += f"{num} ";

print(res.strip());