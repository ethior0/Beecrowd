# corrigir esse depois
# 5
# 10 10 10 10 10
# out esperado: 1
# out meu: 1

# 6
# 10 10 10 10 10 10
# out esperado: 1
# out meu: 2

while True:
  try:
    n = int(input());
    a = [int(x) for x in input().split()];
    
    num = sum(a) / n;
    
    if not(num.is_integer()):
      print(-1);
      continue;
    
    res = 1;
    ini, fim = 0, n-1;  
    while ini < fim and (a[ini] != num or a[fim] != num):
      if a[ini] < num: a[ini] += 1;
      elif a[ini] > num: a[ini] -= 1;
      else: ini += 1;
      
      if a[fim] < num: a[fim] += 1;
      elif a[fim] > num: a[fim] -= 1;
      else: fim -= 1;
      
      if a[ini] == num:
        ini += 1;
      if a[fim] == num:
        fim -= 1;
      
      # print("res e A:", res, a);
      res += 1;
    print(res);
    # print("IDEAL", num)
    # print("A", a);
  except EOFError:
    break;