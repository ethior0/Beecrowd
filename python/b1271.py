cc = 1;

while True:
  n = int(input());
  if n == 0: break;
  
  reverse = [];
  
  r = int(input());
  for _ in range(r):
    i, j = map(int, input().split());
    reverse.append([i, j]);

  q = int(input());
  
  print(f"Genome {cc}");
  for i in range(q):
    k = int(input());
    
    for j in range(r):
      a, b = reverse[j][0], reverse[j][1];
      if k < a or k > b: continue;
      k = a + b - k;
    print(k);
  
  cc += 1;