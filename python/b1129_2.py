res, N = "ABCDE*", 1;

while N != 0:
  N = int(input());
  for i in range(N):
    aux = -1;
    arr = [int(x) for x in input().split()];
    for j in range(5):
      if int(arr[j]) <= 127:
        if aux == -1: 
          aux = j;
        else: 
          aux = 5;
          break;
    print(res[aux]);