n = int(input());
arr = input().split();

ans = "";

for a in arr:
  b = int(a, base=16);
  ans += chr(b);

print(ans);