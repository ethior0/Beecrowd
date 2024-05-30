arr = [int(x) for x in input().split()];
arr.sort();
somaMin = arr[0] + arr[1];
somaMeio = arr[1] + arr[2];

if somaMin > arr[2] or somaMin > arr[3] or somaMeio > arr[3]:
  print("S");
else:
  print("N");