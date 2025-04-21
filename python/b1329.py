while True:
  n = int(input());
  if n == 0: break;
  
  arr = [int(x) for x in input().split()];
  soma = sum(arr);
  
  print(f"Mary won {n-soma} times and John won {soma} times");