s = int(input());

h = int(s / 3600);
s %= 3600;
m = int(s / 60);
s %= 60;
print(f"{h}:{m}:{s}");