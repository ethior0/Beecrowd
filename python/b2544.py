while True: 
  try:
    N = int(input());
    qtd = 0;
  
    while N > 1:
      N -= (N / 2);
      qtd += 1;
    print("Resultado:", qtd);
  except EOFError: break;