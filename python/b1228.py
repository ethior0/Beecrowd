aux = [];

def insertion_sort(v):
  res = 0;
  
  for i in range(1, len(v)):
    j = i;
    k = j - 1;
    
    while k > -1 and (aux[v[j]] - aux[v[k]]) < 0:
      v[j], v[k] = v[k], v[j];
      res += 1;
      j -= 1;
      k -= 1;
  
  return res;

while True:
  try:
    N = int(input());
    ini = [int(x) for x in input().split()];
    fim = [int(x) for x in input().split()];    

    aux = [0 for _ in range(N+1)];
    
    for i, carro in enumerate(fim):
      aux[carro] = i;
    
    print(insertion_sort(ini));
  except EOFError:
    break;