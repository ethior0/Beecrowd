# Tentativa errada, porém nice try

# caso haja um caminho ate a cidade B,  
# o algoritmo sempre optará pela ferrovia
# mesmo que o custo da rodovia seja menor,
# caso nao haja caminho com a ferrovia, 
# ele usará o custo da rodovia.

# 1 2 - 1000 f
# 2 3 - 900 f
# 1900

# 1 2 - 100 f
# 1 3 - 250 f
# 2 4 - 300 f
# 2 5 - 400 r
# 1050

# 1 2 - 50 r
# 2 3 - 60 f
# 3 4 - 50 r
# 4 5 - 60 f
# 220

N, F, R = map(int, input().split());
# cidades | ferrovias | rodovias

fer = [1001 for _ in range(N+1)];
rod = [1001 for _ in range(N+1)];

# cidade A - cidade B - custo
for _ in range(F): # ferrovias
  A, B, C = map(int, input().split());
  if C < fer[B]:
    fer[B] = C;

for _ in range(R): # rodovias
  I, J, K = map(int, input().split());
  if K < rod[J]:
    rod[J] = K;

custo = 0;
for i in range(2, N+1):
  valor = fer[i];
  if valor == 1001 and valor > rod[i]:
    valor = rod[i];
  custo += valor;

print(custo);