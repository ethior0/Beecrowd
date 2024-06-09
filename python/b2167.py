N = int(input());
lista = list(map(int, input().split()));

res = 0;
for i in range(N-1):
  if lista[i] > lista[i+1]:
    res = i+2;
    break;

print(res);