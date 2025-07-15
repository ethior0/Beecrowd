cc = 1;

while True:
  try:
    n = int(input());
    arr = input().split();
    
    if cc != 1:
      print();
    
    aux, f, m = 0, 0, 0;
    for i in range(0, len(arr)-1, 2):
      num = int(arr[i]);
      c = arr[i+1];
      
      if num == n:
        aux += 1;
        if c == "F":
          f += 1;
        else:
          m += 1;
    
    print(f"Caso {cc}:");
    print(f"Pares Iguais: {aux}");
    print(f"F: {f}");
    print(f"M: {m}");
    
    cc += 1;
  except EOFError:
    break;