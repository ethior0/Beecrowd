A, B, C = map(int, input().split());

if A + B > C and B + C > A and A + C > B:
  if A == B and B == C:
    print("Valido-Equilatero");
  elif A != B and B != C and C != A:
    print("Valido-Escaleno");
  else:
    print("Valido-Isoceles");

  aa = A * A;
  bb = B * B;
  cc = C * C;

  if aa + bb == cc or bb + cc == aa or aa + cc == bb:
    print("Retangulo: S");
  else:
    print("Retangulo: N");
else:
  print("Invalido");