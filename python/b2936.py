porcao = [300, 1500, 600, 1000, 150];
total = 225;

for i in range(5):
  qtd = int(input());
  total += qtd * porcao[i];

print(total);