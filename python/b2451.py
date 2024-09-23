N = int(input());
array = [];
maiorComida, comida = 0, 0;

for i in range(N):
  array.append(input());
  for j in range(N):
    pos = j;
    if i % 2 != 0:
      pos = N-j-1;
    
    if array[i][pos] == "o":
      comida += 1;
      if comida > maiorComida: 
        maiorComida = comida;
    elif array[i][pos] == "A": 
      comida = 0;

print(maiorComida)