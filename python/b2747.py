for i in range(7):
  linha = "";
  for j in range(39):
    if i == 0 or i == 6:
      linha += "-";
    else:
      if j == 0 or j == 38:
        linha += "|";
      else: 
        linha += " ";
  print(linha);