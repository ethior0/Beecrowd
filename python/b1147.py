# casas seguras para o cavalo
# sao casas em que não haja 
# peões nas diagonais superiores

cc = 1;
directions = [[-1, -2], [-1, 2], [-2, -1], [-2, 1], [1, -2], [1, 2], [2, -1], [2, 1]];
col = "abcdefgh";

def solveInput(p):
  h = 8 - int(p[0]);
  v = col.index(p[1]);
  return [h + 1, v + 1];

def convert(board, p):
  pos = solveInput(p);
  board[pos[0]][pos[1]] = 1;

def check(i, j):  
  if board[i-1][j-1] == 1 or board[i-1][j+1] == 1:
    return False;
  return True;

while True:
  c = input();
  if c == "0": break;
  
  board = [[0 for _ in range(10)] for _ in range(10)];
  
  for _ in range(8):
    p = input();
    convert(board, p);
  
  res = 0;
  
  posCavalo = solveInput(c);
  i, j = posCavalo[0], posCavalo[1];
  
  for x in range(8):
    proxI = i + directions[x][0];
    proxJ = j + directions[x][1];
    
    if not(1 <= proxI <= 8 and 1 <= proxJ <= 8):
      continue;
    
    if check(proxI, proxJ):
      res += 1;
  
  print(f"Caso de Teste #{cc}: {res} movimento(s).");
  cc += 1;