import math;

primos = [0] * 3502;

def ehPrimo(num):
  if num == 2: return True;
  if num == 1 or num % 2 == 0: return False;
  
  for i in range(3, int(math.sqrt(num)) + 1, 2):
    if num % i == 0:
      return False;
  
  return True;

def listarPrimos():
  j = 0;
  for i in range(2, 32633):
    if ehPrimo(i):
      primos[j] = i;
      j += 1;

listarPrimos();

while True:
  n = int(input())
  if n == 0: break;
  
  sobrevivente = 0;
  for i in range(1, n):
    sobrevivente = (sobrevivente + primos[i-1]) % i;  
  print(sobrevivente);