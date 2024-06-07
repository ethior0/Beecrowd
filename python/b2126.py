numCaso = 1;

while True:
  try:
    n1 = input();
    n2 = input();
    qtdSub, pos = n2.count(n1), n2.rfind(n1);
  
    print(f"Caso #{numCaso}:");
    if qtdSub > 0: 
      print(f"Qtd.Subsequencias: {qtdSub}");
    else: 
      print("Nao existe subsequencia");
    if pos != -1:
      print(f"Pos: {pos+1}");
    print();

    numCaso += 1;
  except EOFError: break;