X = int(input());

print(X);

while X > 9: # executa enquanto ele é maior que 1 digito
  X = X // 10 * 3 + (X % 10);
  print(X);