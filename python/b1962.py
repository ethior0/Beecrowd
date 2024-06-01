# entendi nada do problema, mas a lógica era suave rsrs

N = int(input());

for i in range(N): 
  T = int(input());
  if T >= 2015:
    print(f"{T - 2014} A.C.");
  else:
    print(f"{2015 - T} D.C.");