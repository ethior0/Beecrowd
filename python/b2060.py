N = int(input());
lista = list(map(int, input().split()));
cc2, cc3, cc4, cc5 = 0, 0, 0, 0;

for num in lista:
  if num % 3 == 0: cc3 += 1;
  if num % 2 == 0: cc2 += 1;
  if num % 4 == 0: cc4 += 1;
  if num % 5 == 0: cc5 += 1;

print(f"{cc2} Multiplo(s) de 2");
print(f"{cc3} Multiplo(s) de 3");
print(f"{cc4} Multiplo(s) de 4");
print(f"{cc5} Multiplo(s) de 5");