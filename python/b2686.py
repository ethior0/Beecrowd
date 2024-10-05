import math;

while True:
  try:
    M = float(input());
    
    if M >= 0 and M < 90 or M == 360:
      print("Bom Dia!!");
    elif M >= 90 and M < 180:
      print("Boa Tarde!!");
    elif M >= 180 and M < 270:
      print("Boa Noite!!");
    elif M >= 270 and M < 360:
      print("De Madrugada!!");
    
    horasTotais = 6 + M / 15;
    segundosTotais = round(horasTotais * 3600);
    minutosTotais = segundosTotais / 60;
    segundos = segundosTotais % 60;
    horas = math.trunc(minutosTotais / 60 % 24);
    minutos = math.trunc(minutosTotais % 60);
    
    print(f"{horas:02.0f}:{minutos:02.0f}:{segundos:02.0f}");
  except EOFError: 
    break;