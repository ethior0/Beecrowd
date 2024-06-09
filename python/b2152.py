C = int(input());

for _ in range(C):
  H, M, O = map(int, input().split());

  if O == 0:
    print(f"{H:02}:{M:02} - A porta fechou!");
  else:
    print(f"{H:02}:{M:02} - A porta abriu!");