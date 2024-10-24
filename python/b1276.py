while True:
  try:
    string = "".join(input().split()).strip();
    stringOrd = sorted(string);
    
    res = [];
    if string:
      faixaInicial, faixaFinal = stringOrd[0], stringOrd[0];
    
    for i in range(len(string)-1):
      faixa01 = stringOrd[i];
      faixa02 = stringOrd[i+1];
      
      if ord(faixa02) == ord(faixa01) or ord(faixa02) == ord(faixa01) + 1:
        faixaFinal = faixa02;
      else:
        res.append(f"{faixaInicial}:{faixaFinal}");
        faixaInicial = faixa02;
        faixaFinal = faixa02;
      # fbxeac
      # abcefx
      # a:c e:f x:x
    
    if string: 
      res.append(f"{faixaInicial}:{faixaFinal}");  
    
    print(", ".join(res));
  except EOFError:
    break;