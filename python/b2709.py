def ehPrimo(valor):
  ccPrimo = 1;
  for i in range(2, valor+1):
    if valor % i == 0: ccPrimo += 1;
  
  if ccPrimo == 2: 
    return True;
  else: 
    return False;

while True:
  try:
    M = int(input());
    cc, soma = 0, 0;
    moedas = [];
    
    for _ in range(M):
      moedas.append(int(input()));
      
    N = int(input());
    
    while N * cc < M:
      soma += moedas[M-N*cc-1];
      cc += 1;
  
    if ehPrimo(soma):
      print("You’re a coastal aircraft, Robbie, a large silver aircraft.");
    else:
      print("Bad boy! I’ll hit you.");
  except EOFError:
    break;