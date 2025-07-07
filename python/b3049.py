# lado esquerdo maior -> 1
# lado direito maior -> 2
# ambos lados iguais -> 0

b = int(input());
t = int(input());

areaE = (b + t) * 35;
areaD = (160 * 70) - areaE;

if areaE > areaD:
  print(1);
elif areaD > areaE:
  print(2);
else:
  print(0);