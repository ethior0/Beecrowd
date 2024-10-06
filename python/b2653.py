conjunto = set();
tamanho = 0;

while tamanho <= 10**6:
  try:
    joia = input().strip();
    tamanho += len(joia);
    conjunto.add(joia);
  except EOFError: 
    break;

print(len(conjunto));