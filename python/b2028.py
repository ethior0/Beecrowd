numCaso = 1;

while True:
  try:
    N = int(input());
    qtdNum, sen = 1, "0";

    for i in range(N+1):
      novosNum = f" {i}" * i; 
      sen += novosNum;
      qtdNum += 1 * i;

    if qtdNum == 1: 
      print(f"Caso {numCaso}: {qtdNum} numero");
    else:  
      print(f"Caso {numCaso}: {qtdNum} numeros");
    print(sen.strip());
    print();

    numCaso += 1;
  except EOFError: break;