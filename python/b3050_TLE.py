n = int(input());
linha = input().split();
arr = [];

for i, val in enumerate(linha):
  arr.append([val, i]);

arr.sort(key=lambda x: x[0]);
print(arr);