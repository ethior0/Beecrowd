while True:
  N = int(input());
  if N == 0: break;
  
  A = list(map(int, input().split()));
  
  p = 0;
  for i in range(N):
    anterior = ((i - 1) + N) % N;
    proximo = (i + 1) % N;
    
    if A[i] > A[anterior] and A[i] > A[proximo]:
      p += 1;
    elif A[i] < A[anterior] and A[i] < A[proximo]:
      p += 1;
  
  print(p);