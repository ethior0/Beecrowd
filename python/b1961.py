P, N = map(int, input().split());
pipes = [int(x) for x in input().split()];

for i in range(N-1):
  soma = abs(pipes[i] - pipes[i+1]);
  if soma > P: 
    print("GAME OVER");
    break;
  elif i == N - 2: 
    print("YOU WIN");