def resolveProblema(num, alm):
  if alm == "suco":
    return num * 120;
  elif alm == "morango":
    return num * 85;
  elif alm == "mamao":
    return num * 85;
  elif alm == "goiaba":
    return num * 70;
  elif alm == "manga":
    return num * 56;
  elif alm == "laranja":
    return num * 50;
  elif alm == "brocolis":
    return num * 34;

while True:
  T = int(input());
  if T == 0: break;

  consumo = 0;
  for _ in range(T):
    linha = input().split();
    num = int(linha[0]);
    alimento = linha[1];
    consumo += resolveProblema(num, alimento.strip());

  if consumo > 130:
    print(f"Menos {consumo-130} mg");
  elif consumo < 110:
    print(f"Mais {110-consumo} mg");
  else:
    print(f"{consumo} mg");