n = int(input());

r1 = 0;
r2 = 0;
for i in range(n):
  v = float(input());
  s = input().split();
  
  r2 += v;
  r1 += len(s);
  print(f"day {i+1}: {len(s)} kg");

print(f"{(r1/n):.2f} kg by day");
print(f"R$ {(r2/n):.2f} by day");
