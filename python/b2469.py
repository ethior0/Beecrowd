N = int(input());
lista = list(map(int, input().split()));
ordenada = sorted(lista);

maiorCc, cc = 1, 1;
index = 1;

for i in range(1, N):
  if ordenada[i-1] == ordenada[i]:
    cc += 1;
  else: 
    cc = 1;
  
  if cc > maiorCc or (cc == maiorCc and ordenada[i] > ordenada[index]):
    maiorCc = cc;
    index = i;

print(ordenada[index]);