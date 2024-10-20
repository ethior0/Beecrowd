while True:
  try:
    n = input();
    res = "";
    
    for i in n:
      try:
        if i == "o" or i == "O":
          res += "0";
        elif i == "l":
          res += "1";
        elif i.isalpha() or int(i) >= 0:
          res += i;
      except ValueError: continue;
    
    try:
      if int(res) <= 2147483647:
        print(int(res));
      else: # maior que 2147483647
        print("error");
    except ValueError: # convert e nao eh num
      print("error");
    
  except EOFError: 
    break;