while True:
  try:
    N = int(input());
    M, L = map(int, input().split());

    cartas1 = []; # Marcos
    cartas2 = []; # Leonardo

    for _ in range(M):
      linha = list(map(int, input().split()));
      cartas1.append(linha);
    for _ in range(L):
      linha = list(map(int, input().split()));
      cartas2.append(linha);
  
    Cm, Cl = map(int, input().split());
    A = int(input());

    atributoM = cartas1[Cm-1][A-1];
    atributoL = cartas2[Cl-1][A-1]

    if atributoM > atributoL:
      print("Marcos");
    elif atributoM < atributoL:
      print("Leonardo");
    else:
      print("Empate");
  except EOFError:
    break;