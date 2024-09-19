while True:
  try:
    linha = input().split();
    
    if linha[0] == "papel" and linha[1] == "pedra" and linha[1] == linha[2] or linha[0] == "pedra" and linha[1] == "tesoura" and linha[1] == linha[2] or linha[0] == "tesoura" and linha[1] == "papel" and linha[1] == linha[2]:
      print("Os atributos dos monstros vao ser inteligencia, sabedoria...");
    elif linha[1] == "papel" and linha[0] == "pedra" and linha[0] == linha[2] or linha[1] == "pedra" and linha[0] == "tesoura" and linha[0] == linha[2] or linha[1] == "tesoura" and linha[0] == "papel" and linha[0] == linha[2]:
      print("Iron Maiden's gonna get you, no matter how far!");
    elif linha[2] == "papel" and linha[1] == "pedra" and linha[0] == linha[1] or linha[2] == "pedra" and linha[1] == "tesoura" and linha[0] == linha[1] or linha[2] == "tesoura" and linha[1] == "papel" and linha[0] == linha[1]:
      print("Urano perdeu algo muito precioso...");
    else:
      print("Putz vei, o Leo ta demorando muito pra jogar...");
    
  except EOFError: break;