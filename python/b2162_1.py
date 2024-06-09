N = int(input());
h = list(map(int, input().split()));

length, res = len(h), 0;

# Poggers '-'
if h[0] < h[1]:
  for i in range(length-1):
    if h[i] < h[i+1] and i % 2 == 0:
      res = 1;
    elif h[i] > h[i+1] and i % 2 != 0:
      res = 1;
    else:
      res = 0;
      break;
else:
    for i in range(length-1):
      if h[i] > h[i+1] and i % 2 == 0:
        res = 1;
      elif h[i] < h[i+1] and i % 2 != 0:
        res = 1;
      else:
        res = 0;
        break;

print(res);