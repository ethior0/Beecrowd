while True:
  try:
    N, D = map(int, input().split());
    dataEvento = "";

    for _ in range(D):
      linha = input().split();
      data = linha[0];
      pessoas = list(map(int, linha[1:len(linha)]));
      ccPessoas = pessoas.count(1);
      
      if ccPessoas == N:
        if dataEvento == "":
          dataEvento = data;
        else:
          dataArray = list(map(int, data.replace("/", " ").split(" ")));
          dataEventoArray = list(map(int, dataEvento.replace("/", " ").split(" "))); 
          if dataArray[2] <= dataEventoArray[2] and dataArray[1] <= dataEventoArray[1] and dataArray[0] < dataEventoArray[0]:
            dataEvento = data;

    if dataEvento == "":
      print("Pizza antes de FdI");
    else:
      print(dataEvento);
    
  except EOFError: break;

