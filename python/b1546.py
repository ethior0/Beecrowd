n = int(input());

setor = ["Rolien", "Naej", "Elehcim", "Odranoel"];

for _ in range(n):
  k = int(input());
  
  for _ in range(k):
    ki = int(input());
    print(setor[ki-1]);