N = int(input());

for _ in range(N):
  linha = input();
  flag = True;
  res = "";
  
  for char in linha:
    if char != " ":
      if flag:
        res += char;
        flag = False;
    else:
      flag = True;
  
  print(res);