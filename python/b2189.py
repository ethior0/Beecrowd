cc = 1;

while True:
  n = int(input());
  if n == 0: break;
  
  arr = [int(x) for x in input().split()];
  
  res = 0;
  for i, val in enumerate(arr):
    if i+1 == val:
      res = i+1;
      break;
  
  print(f"Teste {cc}");
  print(res);
  print();
  
  cc += 1;