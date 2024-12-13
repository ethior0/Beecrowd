# a melhor soma é quando há um número maior e outros menores que complete
# a quantidade de tapetes, pois o quadrado do maior número sempre será a
# melhor opção:

# 6 3
# Opção 1 - ter varios tapetes com valores distribuidos (errado)
# 2 * 2 + 2 * 2 + 2 * 2 = 12 (preço)

# Opção 2 - ter 1 tapete com o maior valor e outros menores que completem a quantidade (correto)
# 1 * 1 + 1 * 1 + 4 * 4 = 16 (preço)

# 10 5
# 2 + 2 + 2 + 2 + 2 = 10 (tamanho)
# 2² + 2² + 2² + 2² + 2² = 20 (preço) (errado -> Opção 1)

# 1 + 1 + 1 + 1 + 6 = 10 (tamanho)
# 1² + 1² + 1² + 1² + 6² = 40 (preço) (certo -> Opção 2) 

# 1000000 9
#  + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 999992 = 1000000 (tamanho)
# 1² + 1² + 1² + 1² + 1² + 1² + 1² + 1² + 999992² = 999.984.000.072 (preço)

L, N = map(int, input().split());
L = L - (N - 1);

print(L ** 2 + (N - 1));