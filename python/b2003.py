while True:
  try:
    hour, minute = map(int, input().split(":"));
    seconds = hour * 3600 + minute * 60 + 60 * 60;
    delay = (seconds - 8 * 3600) // 60;

    if delay > 0:
      print(f"Atraso maximo: {delay}")
    else:
      print("Atraso maximo: 0"); 
  except EOFError: break;
