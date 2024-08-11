N = int(input());

for _ in range(N):
  L = int(input());
  lista = [int(x) for x in input().split()];
  swaps = 0;

  print(f"Optimal train swapping takes {swaps} swaps.");