# Um pico em uma forma de onda é um valor de 
# uma amostra que representa um max ou min local,
# ou seja, um ponto de inflexao da forma de onda

# o pico precisa estar entre 2 nums maiores que ele ou
# 2 nums menores q ele; caso contrário, ele não é pico

while True:
  N = int(input());
  if N == 0: break;
  
  A = list(map(int, input().split()));
  p = 0;
  
  atual, pre, suf = 0, 0, 0;
  
  for i in range(1, N-1):
    pre = A[i-1];
    atual = A[i];
    suf = A[i+1];
    
    if (atual > suf and atual > pre) or (atual < suf and atual < pre):
      p += 1;
  
  if (A[N-1] > A[N-2] and A[N-1] > A[0]) or (A[N-1] < A[N-2] and A[N-1] < A[0]):
    p += 1; # checagem do pico do fim das amostras
  if (A[0] > A[N-1] and A[0] > A[1]) or (A[0] < A[N-1] and A[0] < A[1]):
    p += 1; # checagem do pico do inicio das amostras
  
  print(p);