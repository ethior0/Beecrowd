N, M  = map(int, input().split());
array = [];

for i in range(N):
  nums = list(map(int, input().split()));
  array.append(nums);

x, y = 0, 0;
for i in range(1, N-1):
  for j in range(1, M-1):
    if array[i][j] == 42:
      if array[i][j-1] == 7 and array[i][j+1] == 7:
        if array[i+1][j] == 7 and array[i+1][j-1] == 7 and array[i+1][j+1] == 7:
          if array[i-1][j] == 7 and array[i-1][j-1] == 7 and array[i-1][j+1] == 7:
            x, y = i+1, j+1;

print(x, y);