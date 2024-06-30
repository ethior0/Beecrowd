# A vitória vale 2 pontos
# A derrota vale 1 ponto

# Caso haja empates na pontuação do campeonato:
# 1º time com melhor cesta average -> pontos marcados / pontos recebidos
# 2º time que mais marcou pontos
# 3º time com menor num de inscrição

# dic = 0 -> pontos, pontos marcados, pontos recebidos

def insertion_sort(dic):
  n = len(dic);
  for i in range(1, n):
    j = i;
    while j > 0 and dic[j]["p"] >= dic[j-1]["p"]:
      if dic[j]["p"] == dic[j-1]["p"]:
        avg1 = dic[j]["pM"] / dic[j]["pR"];
        avg2 = dic[j-1]["pM"] / dic[j-1]["pR"];
        if (avg1 > avg2) or (dic[j]["pM"] > dic[j-1]["pM"] and avg1 == avg2) or (dic[j-1]["id"] > dic[j]["id"] and avg1 == avg2 and dic[j]["pM"] == dic[j-1]["pM"]):
          dic[j-1], dic[j] = dic[j], dic[j-1];
      else:
        dic[j-1], dic[j] = dic[j], dic[j-1];
      j -= 1;

def checa_vitoria(x, y, z, w, dic):
  if y > w:
    dic[x-1]["p"] += 2;
    dic[z-1]["p"] += 1;
  else:
    dic[x-1]["p"] += 1;
    dic[z-1]["p"] += 2;

h = 1;

while True:
  n = int(input());

  if n == 0: break;
  if n != 0 and h > 1: print();

  dic = [{"id": i+1, "p": 0, "pM": 0, "pR": 0} for i in range(n)];

  for _ in range(n * (n - 1) // 2):
    x, y, z, w = map(int, input().split());
    dic[x-1]["pM"] += y;
    dic[x-1]["pR"] += w;
    dic[z-1]["pM"] += w;
    dic[z-1]["pR"] += y;
    checa_vitoria(x, y, z, w, dic);

  insertion_sort(dic);
  
  sen = "";
  for i in range(len(dic)):
    sen += f'{dic[i]["id"]} ';
  
  print(f"Instancia {h}");
  print(f"{sen.strip()}");
  h += 1;