def countSwaps(arr): 
  cc = 0
  for i in range(len(arr)): 
    for j in range(i+1, len(arr)): 
      if arr[i] > arr[j]: 
        cc += 1
  return cc 

N = int(input());

for _ in range(N):
  L = int(input());
  lista = list(map(int, input().split()));
  print(f"Optimal train swapping takes {countSwaps(lista)} swaps.");