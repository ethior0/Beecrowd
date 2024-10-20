N = int(input());
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

for _ in range(N):
  palavra = input();
  desloc = int(input());
  
  alfabeto_deslocado = alfabeto[-desloc:] + alfabeto[:-desloc];
  tabela = "".maketrans(alfabeto, alfabeto_deslocado)
  
  print(palavra.translate(tabela));