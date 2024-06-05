while True:
  try:
    V = float(input());
    D = float(input());
    raio = D / 2;
    # Volume = PI * raio² * altura
    altura = V / (3.14 * pow(raio, 2));
    area = pow(raio, 2) * 3.14;

    print(f"ALTURA = {altura:.2f}");
    print(f"AREA = {area:.2f}");
  except EOFError: break;