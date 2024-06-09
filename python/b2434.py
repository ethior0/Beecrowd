N, S = map(int, input().split());
menor = S;

for _ in range(N):
  num = int(input());
  S = S + num;
  if S < menor:
    menor = S;

print(menor);