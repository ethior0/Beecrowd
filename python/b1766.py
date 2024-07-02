# Ordenação das ovelhas:
# 1º decrescente por peso (10, 9, 8, ... 1)
# Caso empate:
#   2º ascendente pela idade (1, 2, 3, ... 10)
#   3º ascendente pela altura
#   4º ascendente pelo nome (a, b, c, ... z)

def insertion_sort(dic):
  n = len(dic);
  for i in range(1, n):
    j = i;
    while j > 0:
      if dic[j-1]["peso"] < dic[j]["peso"]:
        dic[j-1], dic[j] = dic[j], dic[j-1];
      elif dic[j-1]["peso"] == dic[j]["peso"] and dic[j-1]["idade"] > dic[j]["idade"]:
        dic[j-1], dic[j] = dic[j], dic[j-1];
      elif dic[j-1]["peso"] == dic[j]["peso"] and dic[j-1]["idade"] == dic[j]["idade"] and dic[j-1]["altura"] > dic[j]["altura"]:
        dic[j-1], dic[j] = dic[j], dic[j-1];
      elif dic[j-1]["peso"] == dic[j]["peso"] and dic[j-1]["idade"] == dic[j]["idade"] and dic[j-1]["altura"] == dic[j]["altura"] and ord(dic[j-1]["nome"][0]) > ord(dic[j]["nome"][0]):
        dic[j-1], dic[j] = dic[j], dic[j-1];
      j -= 1;

T = int(input());

for cc in range(T):
  N, M = map(int, input().split());

  dic = [{} for _ in range(N)];

  for i in range(N):
    S, P, I, A = input().split();
    dic[i]["nome"] = S;
    dic[i]["peso"] = int(P);
    dic[i]["idade"] = int(I);
    dic[i]["altura"] = float(A);

  insertion_sort(dic);

  print(f"CENARIO {{{cc+1}}}");
  for i in range(M):
    print(f"{i+1} - {dic[i]['nome']}");