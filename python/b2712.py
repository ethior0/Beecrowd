import re;

N = int(input());

for _ in range(N):
  S = input();
  
  if re.match("^[A-Z]{3}-[0-9]{4}$", S) != None:
    ultimo = S[len(S)-1];
    if ultimo == "1" or ultimo == "2":
      print("MONDAY");
    elif ultimo == "3" or ultimo == "4":
      print("TUESDAY");
    elif ultimo == "5" or ultimo == "6":
      print("WEDNESDAY");
    elif ultimo == "7" or ultimo == "8":
      print("THURSDAY");
    else:
      print("FRIDAY");
  else:
    print("FAILURE");