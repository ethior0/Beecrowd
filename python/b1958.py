import math;

def pegarSinal(sinal):
  if sinal == 1: return "+";
  return "-";

X = float(input());

print(f"{pegarSinal(math.copysign(1, X))}{abs(X):.4E}");