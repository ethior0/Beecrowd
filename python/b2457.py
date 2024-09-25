letra = input().strip();
texto = input().split();
ccLetra = 0;

for palavra in texto:
  if palavra.count(letra) > 0: ccLetra += 1;

print(f"{(ccLetra / len(texto) * 100):.1f}")