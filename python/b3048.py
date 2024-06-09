N = int(input());
num = int(input());
cc, aux = 1, num;

for i in range(1, N):
  num = int(input());
  if aux != num:  
    cc += 1;
  aux = num;

print(cc);