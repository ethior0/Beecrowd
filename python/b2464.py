alfabeto = "abcdefghijklmnopqrstuvwxyz";
alf = input(); # 0 1 2 3 ... 25
frase = input();

res = "";
for letra in frase:
  i = alfabeto.index(letra);
  res += alf[i];

print(res);
