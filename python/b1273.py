# mesmo codigo do b1278

N = int(input());

while N != 0:
  texto = [];
  tam = 0;
  
  for i in range(N):
    texto.append(" ".join(input().split()));
    if len(texto[i]) > tam:
      tam = len(texto[i]);
  
  for j in range(N):
    print(f"{texto[j]:>{tam}}");
  
  N = int(input());
  if N != 0: print();