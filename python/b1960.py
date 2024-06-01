dic = {
  900: "CM", 500: "D", 400: "CD",
  100: "C", 90: "XC", 50: "L",
  40: "XL", 10: "X", 9: "IX",
  5: "V", 4: "IV", 1: "I",
}

N, sen = int(input()), "";

for num, sym in zip(dic.keys(), dic.values()):
  if N == 0: break;
  
  res = N // num;
  N = N % num;
  if res != 0:
    sen += sym * res;

print(sen);

