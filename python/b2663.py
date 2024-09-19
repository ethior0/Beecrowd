N = int(input());
K = int(input());
lista, cc, cc2 = [], 0, 0;

for _ in range(N):
  num = int(input());
  lista.append(num);

lista.sort(reverse=True);

for i in range(N):
  if cc < K:
    cc += 1;
  elif cc == K and lista[i] == lista[i-1]:
    cc2 += 1;
  else: break;

print(cc+cc2);