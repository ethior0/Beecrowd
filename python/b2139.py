while True:
  try:
    month, daysM = map(int, input().split());
    day = 0;
    for i in range(month-1):
      newI = i + 1;
      if newI == 1 or newI == 3 or newI == 5 or newI == 7 or newI == 8 or newI == 10 or newI == 12:
        day += 31;
      elif newI == 2: day += 29;
      else: day += 30;
    day += daysM;

    if day == 360:
      print("E natal!");
    elif day == 359:
      print("E vespera de natal!");
    elif day > 360:
      print("Ja passou!");
    elif day < 359:
      print(f"Faltam {360 - day} dias para o natal!");
  except EOFError: break;