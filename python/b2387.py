cons = [];
N = int(input());

for i in range(N):
  x, y = map(int, input().split());
  cons.append([x, y]);

cons.sort(key=lambda val: val[1]);

cc, final = 0, 0;

for j in range(N):
  if cons[j][0] >= final:
    cc += 1;
    final = cons[j][1];

print(cc);