T = int(input());

for _ in range(T):
  N = int(input());
  
  nomes = input().split();
  frequencia = input().split();
  res = "";
  
  for i in range(N):
    ccP = frequencia[i].count("P");
    ccM = frequencia[i].count("M");
    presenca = ccP / abs(len(frequencia[i]) - ccM);
    
    if presenca < 0.75:
      res += nomes[i] + " ";
  
  print(res.strip());