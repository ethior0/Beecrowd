N = int(input());

for _ in range(N):
  valores = input().split();
  A = valores[0];
  B = valores[1];
  
  if A[-(len(B)):] == B:
    print("encaixa");
  else: 
    print("nao encaixa");