# se o NUM de ovelhas for:
# IMPAR -> i + 1 (vai pro proximo)
# PAR -> i - 1 (vai pro anterior)

# ovelhas atacadas: 12
# 0 (1 - Impar)
# 2 (3 - Impar)
# 4 (5 - Impar)
# 6 (7 - Impar)
# 10 (11 - Impar)
# 12 (13 - Impar)
# 15 (15 - Par)
# 11 (12 - Par)
# 10 (10 - Par)
# 6 (6 - Par)
# 4 (4 - Par)
# 2 (2 - Par)
# 0 (0 - Par) - Nao tirou
# Chegou ao final. Termina

# ovelhas atacadas: 8
# 0 (1 - Impar)
# 2 (3 - Impar)
# 4 (5 - Impar)
# 6 (7 - Impar)
# 10 (11 - Impar)
# 12 (13 - Impar)
# 16 (17 - Impar)
# 18 (19 - Impar)
# Chegou ao final. Termina.

N = int(input());
arr = [int(x) for x in input().split()];
dic = {};

for num in arr:
  dic[num] = False;

print(dic);
