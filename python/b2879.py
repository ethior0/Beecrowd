n = int(input());

cc = 0;
for _ in range(n):
  p = int(input());
  if p != 1:
    cc += 1;

print(cc);