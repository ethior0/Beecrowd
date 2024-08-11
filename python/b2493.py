def resolverProblema(num1, num2, res, op):
  if op == "+" and num1 + num2 == res:
    return True;
  elif op == "-" and num1 - num2 == res:
    return True;
  elif op == "*" and num1 * num2 == res:
    return True;
  elif op == "I" and num1 + num2 != res and num1 - num2 != res and num1 * num2 != res:
    return True;
  else:
    return False;

while True:
  try:
    T = int(input());

    dicOp = {};
    for i in range(T):
      arr = list(map(int, input().replace("=", " ").split()));
      dicOp[i+1] = arr;
    
    reprovados, cc = "", 0;
    for j in range(T):
      N, E, R = input().split();
      num1 = dicOp[int(E)][0];
      num2 = dicOp[int(E)][1];
      res = dicOp[int(E)][2];

      respostaCerta = resolverProblema(num1, num2, res, R);
      if respostaCerta: cc += 1;
      else: reprovados += N + " ";
  
    if cc == 0:
      print("None Shall Pass!");
    elif cc == T:
      print("You Shall All Pass!");
    else:
      reprovados = reprovados.strip();
      listaNomes = reprovados.split();
      listaNomes.sort();
      print(" ".join(listaNomes));
  except EOFError:
    break;