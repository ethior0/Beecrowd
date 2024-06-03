dic = {
  1001: 1.50, 
  1002: 2.50, 
  1003: 3.50, 
  1004: 4.50, 
  1005: 5.50
};

p = int(input());
soma = 0;

for i in range(p):
  num, qtd = map(int, input().split());
  soma += dic[num] * qtd;

print(f"{soma:.2f}");
