N = int(input());
# dic = {"A": [1, 100], "B: [2, 111]"}

while N != 0:
  dic = {};
  S, P = 0, 0;
  
  for _ in range(N):
    cod, tempo, res = map(str, input().split());
    
    aux = [0, 0];
    
    if dic.get(cod):
      aux = dic[cod];
    else:
      dic[cod] = [1, 0];
    
    aux[0] += 1;
    
    if res == "correct":
      aux[1] = int(tempo);
      P += aux[1] + (aux[0] - 1) * 20;
      S += 1;
    dic[cod] = aux;

  print(S, P);
  N = int(input());