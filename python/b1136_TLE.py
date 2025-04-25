while True:
  n, b = map(int, input().split());
  if n == b == 0: break;
  
  arr = [int(x) for x in input().split()];
  aux = set();
  
  for i in range(b):
    for j in range(i+1, b):
        aux.add(abs(arr[i]-arr[j]));
  
  if len(aux) == n + 1:
    print("Y");
  else:
    print("N");