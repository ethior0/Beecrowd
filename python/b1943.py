# "as pessoas geralmente se colocam na
# menor categoria a qual pertencem"

K = int(input());
res = 100;

if K == 1: res = 1; # top 1
elif K <= 3: res = 3; # top 3
elif K <= 5: res = 5; # top 5
elif K <= 10: res = 10; # top 10
elif K <= 25: res = 25; # top 25
elif K <= 50: res = 50; # top 50

print(f"Top {res}");