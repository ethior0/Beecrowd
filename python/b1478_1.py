#     0 1 2 3 4 5 6 7
# 5 - 1 2 3 4 5 4 3 2

while True:
  n = int(input());
  if n == 0: break;
  
  seq = [];
  
  for i in range(1, n+1):
    seq.append(i);
  for i in range(n-1, 1, -1):
    seq.append(i);

  for j in range(n):
    res = "";
    linha = seq[n+(n-2)-j:n+(n-2)] + seq[0:n-j];
    for i, s in enumerate(linha):
      s = int(s);
      if i == 0:
        res += f"{s:3}";
      else:
        res += f" {s:3}";
    print(res);
  print();
