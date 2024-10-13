N = int(input());

for _ in range(N):
  palavra = input();
  desloc = int(input());
  res = "";
  
  for letra in palavra:
    codLetra = ord(letra);
    codOriginal = codLetra - desloc;
    
    if codOriginal < 65:
      res += chr(codLetra + (26 - desloc));
    else:
      res += chr(codOriginal);
  print(res);