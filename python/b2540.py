while True:
  try:
    N = int(input());
    votos = list(map(int, input().split()));
  
    voto1 = votos.count(1);

    if voto1 >= N * 2 / 3:
      print("impeachment");
    else:
      print("acusacao arquivada");

  except EOFError:
    break;