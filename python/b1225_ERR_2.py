while True:
  try:
    n = int(input());
    a = [int(x) for x in input().split()];
    
    num = sum(a) / n;
    
    if not(num.is_integer()):
      print("Res", -1);
      continue;
    
    res = 1;
    l, r = 0, n-1;
    
    num = int(num);
    
    # 20 10 10 20
    
    while l < r and (a[l] != num or a[r] != num):
      print(a[l], a[r]);
      difLeft = abs(num-a[l]);
      difRight = abs(num-a[r]);
      
      minimo = min(difLeft, difRight);
      
      if a[l] < a[r] and a[r] - difLeft >= 0:
        a[l] += difLeft;
        a[r] -= difLeft;
        res += difLeft;
      elif a[l] > a[r] and a[l] - difRight >= 0:
        a[l] -= difRight;
        a[r] += difRight;
        res += difRight;
      
      if a[l] == num:
        l += 1;
      if a[r] == num:
        r -= 1;
    
    print("Res", res);
  except EOFError:
    break;