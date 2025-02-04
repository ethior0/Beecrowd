while True:
  h1, m1, h2, m2 = map(int, input().split());
  if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
    break;

  mins = 0;
  if h1 > h2:
    mins = (((h2 + 24) * 60) + m2) - (h1 * 60 + m1);
  elif h1 < h2:
    mins = (h2 * 60 + m2) - (h1 * 60 + m1)
  else: # horas iguais
    if m1 > m2:
      mins = (((h2 + 24) * 60) + m2) - (h1 * 60 + m1);
    else:
      mins = m2 - m1;
  
  print(mins);