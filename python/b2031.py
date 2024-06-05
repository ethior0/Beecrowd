def check_winner(p1, p2):
  if p1 == p2 and p1 == "papel": return "Ambos venceram";
  if p1 == p2 and p1 == "pedra": return "Sem ganhador";
  if p1 == p2 and p1 == "ataque": return "Aniquilacao mutua";

  if p1 == "ataque" and p2 == "pedra": return "Jogador 1 venceu";
  elif p1 == "pedra" and p2 == "ataque": return "Jogador 2 venceu";

  if p1 == "pedra" and p2 == "papel": return "Jogador 1 venceu";
  elif p1 == "papel" and p2 == "pedra": return "Jogador 2 venceu";

  if p1 == "ataque" and p2 == "papel": return "Jogador 1 venceu";
  elif p1 == "papel" and p2 == "ataque": return "Jogador 2 venceu";

N = int(input());

for _ in range(N):
  p1 = input();
  p2 = input();
  print(check_winner(p1, p2));