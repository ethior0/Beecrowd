listD = list(map(int, input().split()));
listR = list(map(int, input().split()));
cc = 0;

for i in range(len(listD)):
  if listD[i] - listR[i] < 0:
    cc += listR[i] - listD[i];
print(cc);