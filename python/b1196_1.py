tec = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
  try:
    linha = input();
    
    res = "";
    for i in linha:
      if i in "QAZ` ":
        res += i;
      else:
        res += tec[tec.index(i)-1];
    
    print(res);
  except EOFError:
    break;