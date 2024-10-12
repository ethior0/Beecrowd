N = int(input());

for _ in range(N):
  dieta = list(input());
  cafe = input();
  almoco = input();
  
  cafeAlmoco = list(cafe + almoco);
  cheat = False;
  
  for i in range(len(cafeAlmoco)):
    try:
      dieta.remove(cafeAlmoco[i]);
    except ValueError:
      cheat = True;
      break;
  
  if cheat:
    print("CHEATER");
  else:
    print("".join(sorted(dieta)));