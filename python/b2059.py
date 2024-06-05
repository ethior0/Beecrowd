p, j1, j2, r, a = map(int, input().split());
vencedor, soma = 0, j1+j2;

# 0 -> impar | 1 -> 
if soma % 2 != 0 and p == 0: vencedor = 1;
elif soma % 2 == 0 and p == 1: vencedor = 1;
else: vencedor = 2;

if r == 1 and a == 1: vencedor = 2;  
elif r == 1 and a == 0: vencedor = 1;  
elif r == 0 and a == 1: vencedor = 1;

if vencedor == 1: 
  print("Jogador 1 ganha!");
elif vencedor == 2:
  print("Jogador 2 ganha!");