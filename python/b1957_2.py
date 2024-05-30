hexa, res = "0123456789ABCDEF", "";
V = int(input());

while V / 16 != 0:
  resto = V % 16;
  V = V // 16;
  res += hexa[int(resto)];

print(res[::-1]);