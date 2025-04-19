cc = 1;

while True:
  n = int(input());
  if n == 0: break;
  
  g = [x for x in range(n+1)];
  
  r = int(input());
  for _ in range(r):
    i, j = [int(x) for x in input().split()];
    while i < j:
      g[i], g[j] = g[j], g[i];
      i += 1;
      j -= 1;
  
  res = [];
  
  q = int(input());
  for _ in range(q):
    k = int(input());
    res.append(g[k]);
  
  print(f"Genome {cc}");
  for v in res:
    print(v);
  
  cc += 1;