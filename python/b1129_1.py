def letraQuestao(i):
  if i == 0: return "A";
  elif i == 1: return "B";
  elif i == 2: return "C";
  elif i == 3: return "D";
  elif i == 4: return "E";
  return "*";

N = 1;

while N != 0:
  N = int(input());
  for i in range(N):
    arr, aux = [], -1;
    A, B, C, D, E = map(arr.append, input().split(" "));
    for j in range(5):
      if int(arr[j]) <= 127:
        if aux == -1: 
          aux = j;
        else: 
          aux = -2;
          break;
    print(letraQuestao(aux));
