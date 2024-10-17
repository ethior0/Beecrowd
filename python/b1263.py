while True:
  try:
    texto = input().lower().split();
    
    letra0 = texto[0][0];
    aliteracao = 0;
    flag = False;
    
    for i in range(1, len(texto)):
      letra1 = texto[i][0];
      if letra1 == letra0:
        if not flag:
          aliteracao += 1;      
          flag = True;
      else:
        flag = False;
      letra0 = texto[i][0];
    
    print(aliteracao);
  except EOFError:
    break;