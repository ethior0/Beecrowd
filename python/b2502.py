while True:
  try:
    C, N = map(int, input().split());
    cifra1 = str(input());
    cifra2 = str(input());
    for _ in range(N):
      frase = str(input());
      for i in range(C): 
        frase = frase.replace(cifra1[i].lower(), "ç").replace(cifra1[i].upper(), "Ç");
        frase = frase.replace(cifra2[i].lower(), "á").replace(cifra2[i].upper(), "Á");
        frase = frase.replace("ç", cifra2[i].lower()).replace("Ç", cifra2[i].upper());
        frase = frase.replace("á", cifra1[i].lower()).replace("Á", cifra1[i].upper());
      print(frase);
    print();
  except EOFError:
    break;