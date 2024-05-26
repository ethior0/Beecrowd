# TIME LIMIT EXCEEDED :|

N = int(input());
cc = 1;

while N != 0:
  residents = 0;
  totalC = 0;
  sen = "";
  array = [];
  
  for i in range(N):
    X, Y = map(int, input().split(" "));
    residents += X;
    totalC += Y;
    array.append([int(Y/X), X]);
  
  array.sort();

  j = 0;
  while j < N:
    innerArray = array[j];
    if j + 1 < N - 1:
      nextArray = array[j+1];
      if innerArray[0] == nextArray[0]:
        sum = innerArray[1] + nextArray[1];
        sen += f"{sum}-{innerArray[0]} ";
        array.pop(j+1);
        N -= 1;
        j += 1;
        continue;
    sen += f"{innerArray[1]}-{innerArray[0]} ";
    j += 1;

  print(f"Cidade# {cc}:");
  print(sen.strip());
  print(f"Consumo medio: {(totalC/residents):.2f} m3.\n");

  cc += 1;
  N = int(input());