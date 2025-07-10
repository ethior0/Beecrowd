c = int(input());
arr = [int(x) for x in input().split()];

cc = 0;

for i in arr:
  if i == 1: cc += 1;

print(cc);