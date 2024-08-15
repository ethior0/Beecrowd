while True:
  try:
    N, M = map(int, input().split());
    matriz = [];
  
    for _ in range(N):
      linha = list(input().replace("1", "9").split());
      matriz.append(linha);

    p = 0;
    for i in range(N):
      for j in range(M):
        if matriz[i][j] == "0":
          if (i > 0): 
            if (matriz[i-1][j] == "9"): p += 1;
          if (i < N-1): 
            if (matriz[i+1][j] == "9"): p += 1;
          if (j > 0): 
            if (matriz[i][j-1] == "9"): p += 1; 
          if (j < M-1): 
            if (matriz[i][j+1] == "9"): p += 1; 
          matriz[i][j] = str(p);
          p = 0;
      print("".join(matriz[i]));
  except EOFError:
    break;