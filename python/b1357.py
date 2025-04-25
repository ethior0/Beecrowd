braille = [".***..", "*.....", "*.*...", "**....", "**.*..", "*..*..", "***...", "****..", "*.**..", ".**..."];

while True:
  d = int(input());
  if d == 0: break;
  l = input();

  if l == "S":
    msg = input();
    
    linha1, linha2, linha3 = "", "", "";
    for i in msg:
      i = int(i);
      linha1 += f"{braille[i][0]}{braille[i][1]} ";
    
    for i in msg:
      i = int(i);
      linha2 += f"{braille[i][2]}{braille[i][3]} ";
    
    for i in msg:
      i = int(i);
      linha3 += f"{braille[i][4]}{braille[i][5]} ";
    
    print(linha1.strip());
    print(linha2.strip());
    print(linha3.strip());
  else:
    nums = ["" for _ in range(d)];
    
    for _ in range(3):
      linha = input().split();
      for i, num in enumerate(linha):
        nums[i] += num;
    
    res = "";
    for j in nums:
      numero = braille.index(j);
      res += str(numero);
    
    print(res);