N = int(input());
tri = [list(map(int, input().split()))];

cc = 0;

# iguais -> preta (1)
# diferentes -> branca (-1)

while cc < N:
  arr = [];
  for i in range(1, N-cc):
    if tri[cc][i-1] == tri[cc][i]: 
      arr.append(1); 
    else: 
      arr.append(-1);
  if arr:
    tri.append(arr);
  cc += 1;

valor = tri[cc-1][0];

if valor == 1:
  print("preta");
else:
  print("branca");