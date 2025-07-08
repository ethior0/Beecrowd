def raf(x, y):
  return (3 * x) ** 2 + (y ** 2);

def bet(x, y):
  return 2 * (x ** 2) + (5 * y) ** 2;

def car(x, y):
  return (-100 * x) + (y ** 3);

n = int(input());

for _ in range(n):
  x, y = map(int, input().split());
  
  r = raf(x, y);
  b = bet(x, y);
  c = car(x, y);
  
  if r > b and r > c:
    print("Rafael ganhou");
  elif b > r and b > c:
    print("Beto ganhou");
  else:
    print("Carlos ganhou");