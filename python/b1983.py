n = int(input());
bestNum, bestNote = -1, 8;

for i in range(n):
  num, note = map(float, input().split());
  if note >= bestNote:
    bestNum = num;
    bestNote = note;

if bestNum == -1: print("Minimum note not reached");
else: print(f"{bestNum:.0f}");