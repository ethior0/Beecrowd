import re;

def substituirTag(texto, tag, valor):
  return re.sub(tag, valor, texto, flags=re.IGNORECASE);

while True:
  try:
    tag = input();
    valor = input();
    linha = input();
    
    inicial = None;
    res = "";
    
    for i in range(len(linha)):
      if linha[i] == "<":
        inicial = i;
      elif linha[i] == ">" and inicial != None:
        novaTag = substituirTag(linha[inicial:i+1], tag, valor);
        res += novaTag;
        inicial = None;
      elif inicial == None:
        res += linha[i];
      # esse código não trata tags nao finalizadas
    
    print("RESPOSTA", res);
  except EOFError:
    break;