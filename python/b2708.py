linha = input().split();
ccT, ccJ = 0, 0;

while linha[0] != "ABEND":
  acao = linha[0];
  T = int(linha[1]);
  
  if acao == "SALIDA":
    ccT += T;
    ccJ += 1;
  else:
    ccT -= T;
    ccJ -= 1;
  
  linha = input().split();

print(ccT);
print(ccJ);