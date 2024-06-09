N = int(input());
soma = 0;

for _ in range(N):
  T, V = map(int, input().split());
  soma += T * V;

print(soma);