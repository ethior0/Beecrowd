while True:
  try:
    texto = input();
    
    ccI = texto.count("_");
    ccN = texto.count("*");
    newTexto = "";
    
    for letra in texto:
      if letra == "_":
        if ccI % 2 == 0:
          newTexto += "<i>";
        else:
          newTexto += "</i>";
        ccI -= 1;
      elif letra == "*":
        if ccN % 2 == 0:
          newTexto += "<b>";
        else:
          newTexto += "</b>";
        ccN -= 1;
      else:
        newTexto += letra;
    
    print(newTexto);
  except EOFError:
    break;