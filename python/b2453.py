palavras = input().split();
newPalavras = [];

for i in range(len(palavras)):
  palavra = "";
  for j in range(len(palavras[i])):
    if j % 2 != 0:
      palavra += palavras[i][j];
  newPalavras.append(palavra);

print(" ".join(newPalavras));