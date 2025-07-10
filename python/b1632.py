t = int(input());

v = "aeiosAEIOS"

for _ in range(t):
  cc = 1;
  s = input();
  
  for l in s:
    if l in v: cc *= 3
    else: cc *= 2
  print(cc);