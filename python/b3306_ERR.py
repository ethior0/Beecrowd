# problema com input bugado

import math;

while True:
  try:
    N, Q = map(int, input().split());
    vetor = list(map(int, input().split()));
    
    for i in range(Q):
      linha = list(map(int, input().split()));          
      A = linha[1];
      B = linha[2];
      
      mdc = vetor[A-1];
      
      for j in range(A-1, B):
        if linha[0] == 1:
          vetor[j] += linha[3];
        else:
          mdc = math.gcd(mdc, vetor[j]);
      
      if linha[0] == 2:
        print(mdc);
  except EOFError: break;