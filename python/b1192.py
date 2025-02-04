N = int(input());

for _ in range(N):
  seq = input();
  num1, letra, num2 = int(seq[0]), seq[1], int(seq[2]);
  res = 0;
  
  if num1 == num2:
    res = num1 ** 2;
  elif letra.isupper():
    res = num2 - num1;
  elif letra.islower():
    res = num1 + num2;
  
  print(res);