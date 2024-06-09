S = input();

if S.count("1") % 2 == 0:
  S += "0";
else:
  S += "1";

print(S);