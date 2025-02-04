# sei lá, o input do problema é todo bugado :/

D = int(input());

for i in range(D):
  try:
    linha = input().split(" ");
    
    N = int(linha[0]);
    U = linha[1];
    S = linha[2];

    letraS = S.replace("_", "");
    indexS = S.index(letraS);
    
    aneisArray = [];
    
    for j in range(N):
      anel = input();  
      anel = anel * 2
      aneisArray.append(anel);
    
    aux = aneisArray[indexS];
    indexLetraAux = aux.find(U[indexS]);
    novoAnel = aux[indexLetraAux:len(aux)];
    
    diferenca = novoAnel.find(letraS);  

    palavra = "";
    
    for k in range(N):
      letra = U[k];
      anelAtual = aneisArray[k];
      
      indexLetra = anelAtual.find(letra);
      palavra += anelAtual[indexLetra + diferenca];
    
    print(f"{U} {palavra}");
  except ValueError:
    pass;