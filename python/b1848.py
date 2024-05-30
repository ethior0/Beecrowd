cc, soma = 0, 0;
while True:
  if cc == 3: break;
  
  line = input();
  if line == "caw caw":
    print(soma);
    cc += 1;
    soma = 0;
  else:
    value = line.replace("-", "0").replace("*", "1");
    soma += int(value, 2);