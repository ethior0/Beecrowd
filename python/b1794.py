n = int(input());
la, lb = [int(x) for x in input().split()];
sa, sb = [int(x) for x in input().split()];

if (n >= la and n <= lb) and (n >= sa and n <= sb):
  print("possivel");
else:
  print("impossivel");