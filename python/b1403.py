while True:
  n, m = map(int, input().split());
  if n == 0 and m == 0: break;

  dic = {};
  
  for _ in range(n):
    linha = list(map(int, input().split()));
    for i in linha:
      dic[i] = dic.get(i, 0) + 1;

  melhor, segundoMelhor = 0, 0;
  melhorArr, segundoMelhorArr = [], [];
  
  for key, count in dic.items():
    if count > melhor:
      segundoMelhor = melhor;
      segundoMelhorArr = melhorArr;
      melhor = count;
      melhorArr = [key];
    elif count == melhor:
      melhorArr.append(key);
    elif count > segundoMelhor:
      segundoMelhor = count;
      segundoMelhorArr = [key];
    elif count == segundoMelhor:
      segundoMelhorArr.append(key);
  
  ans = "";
  for i in sorted(segundoMelhorArr):
    ans += f"{i} ";
  
  print(ans);