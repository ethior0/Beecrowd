l, d = map(int, input().split());
k, p = map(int, input().split());

qtdP = l // d;

# l km * valor km + qtdP pedagios * valor pedagio
print((l * k) + (qtdP * p));