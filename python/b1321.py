# backtracking
def checar(idx, win):
  if idx == 3:
    return win >= 2;

  for j in range(3):
    if cons[j]:
      continue;
    
    cons[j] = True;
    
    if (not(checar(idx + 1, win + (1 if arrB[idx] > arrA[j] else 0)))):
      return False;
    
    cons[j] = False;
  return True;

while True:
  a, b, c, x, y = [int(x) for x in input().split()];
  if a == b == c == x == y == 0: break;

  arrA = [a, b, c];
  arrB = [x, y, 0];

  i = 0;
  for i in range(1, 54):
    flag = True;
    for k in range(3):
      if arrA[k] == i: flag = False;
    
    for k in range(2):
      if arrB[k] == i: flag = False;
    
    if not(flag):
      continue;

    arrB[2] = i;
    cons = [False, False, False];
    
    if checar(0, 0):
      break;
  
  if i == 53:
    print(-1);
  else:
    print(i);