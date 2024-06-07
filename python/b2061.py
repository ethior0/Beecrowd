N, M = map(int, input().split());

for _ in range(M):
  act = input();
  if act == "fechou": N += 1;
  else: N -= 1;

print(N);