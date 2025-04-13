# incompleto

while True:
  # pos do rafael
  x, y = map(int, input().split());
  if not(x) and not(y): break;
  
  arr = [];
  
  for i in range(3):
    x, y, c = input().split();
    arr.append([int(x), int(y), c]);
  
  print(arr);