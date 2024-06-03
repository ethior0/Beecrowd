T, guess, cc = int(input()), input().split(), 0;

for g in guess:
  if int(g) == T: cc += 1;
print(cc);