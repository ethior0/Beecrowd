fibArr = [0, 1];
qtdArr = [1, 1];
cc = 0;

def fib(n):
  global cc;
  cc += 1;
  
  if len(fibArr)-1 >= n:
    return fibArr[n];
  
  a, b = fib(n-1), fib(n-2);
  
  fibArr.append(a + b);
  qtdArr.append(qtdArr[n-1] + qtdArr[n-2] + 1);
  
  return fibArr[n];

n = int(input());

for _ in range(n):
  x = int(input());
  result = fib(x);
  
  print(f"fib({x}) = {qtdArr[x] - 1} calls = {result}");
  
  cc = 0;