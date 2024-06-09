N = int(input());
H = list(map(int, input().split()));

if H[0] == H[1]:
  res = 0;
else:
  res = 1;
  for i in range(1, N-1):
    if not ((H[i] < H[i+1] and H[i] < H[i-1]) or (H[i] > H[i+1] and H[i] > H[i-1])):
      res = 0;
      break;

print(res);