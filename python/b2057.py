S, T, F = map(int, input().split());
if S == 0: S = 24;

res = (S + T) % 24 + F;
if res < 0: res += 24;

print(res);