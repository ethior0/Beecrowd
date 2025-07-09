n = int(input());

ans = 0;
for _ in range(n):
  l, c = map(int, input().split());
  if l > c: ans += c;

print(ans);