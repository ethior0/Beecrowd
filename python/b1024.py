N, cc = int(input()), 0;

while cc < N:
  text = input();
  newText, length, j = "", len(text) / 2, 0;

  for i in text:    
    if i.isalpha(): # 0 1 2 3 4 5 6 7 8 (9 / 2 -> 4.5 ou 4)
      if j < length: newText += chr(ord(i) + 2);
      else: newText += chr(ord(i) + 3);
    else: 
      if j < length: newText += chr(ord(i) - 1);
      else: newText += i;
    j += 1;
  
  print(f"{newText[::-1]}");
  cc += 1;