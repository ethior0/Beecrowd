F1, F2 = map(float, input().split());
# convertendo porcentagem
F1 /= 100;
F2 /= 100;

i = (1 + F1) * (1 + F2) * 100;
i -= 100;

print(f"{i:.6f}");