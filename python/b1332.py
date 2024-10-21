def checaPalavra(palavra):
  cc1, cc2 = 0, 0;
  
  if palavra[0] == "o": cc1 += 1;
  elif palavra[0] == "t": cc2 += 1;
  if palavra[1] == "n": cc1 += 1;
  elif palavra[1] == "w": cc2 += 1;
  if palavra[2] == "e": cc1 += 1;
  elif palavra[2] == "o": cc2 += 1;
  
  return 1 if cc1 > cc2 else 2;

N = int(input());

for _ in range(N):
  palavra = input();
  
  if len(palavra) == 3: 
    print(checaPalavra(palavra));
  else: 
    print(3);