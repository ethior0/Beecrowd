alf = "abcdefghijklmnopqrstuvwxyz";

T = int(input());

for _ in range(T):
  A, B = input().split();
  cc = 0;
  
  for j in range(len(A)):
    letraA = alf.index(A[j]);
    letraB = alf.index(B[j]);
    cc += (letraB - letraA) % 26;
  
  print(cc);