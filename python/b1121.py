def verificaDir(char):
  if char == "N": return 0;
  elif char == "L": return 1;
  elif char == "S": return 2;
  else: return 3;

while True:
  n, m, s = map(int, input().split());
  if n == 0 and m == 0 and s == 0:
    break;
  
  board = [];
  # "." -> 0 (vazia)
  # "#" -> 1 (nao pode passar)
  # "*" -> 2 (figurinha)
  # "N, S, L, O" -> 3 (robo)

  # N L S O
  direction = [[-1, 0], [0, 1], [1, 0], [0, -1]];
  # dirAtual = 0;
  # D -> dirAtual + 1 % 4; 
  # E -> dirAtual - 1 % 4;

  posAtual = [0, 0];
  dirAtual = 0;

  for i in range(n):
    linha = input();
    linhaArray = [];
    
    for j in range(m):
      char = linha[j];
      
      if char == ".": linhaArray.append(0);
      elif char == "#": linhaArray.append(1);
      elif char == "*": linhaArray.append(2);
      else: # direção e posicao do robo
        linhaArray.append(3);
        dirAtual = verificaDir(char);
        posAtual[0], posAtual[1] = i, j;
    board.append(linhaArray);

  seq = input();

  res = 0;
  for s in seq:
    if s == "D":
      dirAtual = (dirAtual + 1) % 4;
    elif s == "E":
      dirAtual = (dirAtual - 1) % 4;
    else:
      auxX, auxY = posAtual[0] + direction[dirAtual][0], posAtual[1] + direction[dirAtual][1];
      
      # caso fora do board ou caso haja pilastra
      if auxX < 0 or auxX > n-1 or auxY < 0 or auxY > m-1:
        continue;
      if board[auxX][auxY] == 1:
        continue;
      
      # troco a pos atual por celula vazia
      board[posAtual[0]][posAtual[1]] = 0;
      
      # caso haja figurinha, aumenta res
      if board[auxX][auxY] == 2:
        res += 1;
      
      # mudo a pos atual do robo
      board[auxX][auxY] = 3;
      posAtual[0], posAtual[1] = auxX, auxY;

  print(res);