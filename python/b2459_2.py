# Solução utilizando a implementação do algoritmo de Kraskal do site: https://www.mycompiler.io/view/5X3yswaDSrL

class Subconjunto: 
  def __init__(self, pai, classificacao):
    self.pai = pai;
    self.classificacao = classificacao;

class Aresta:
  def __init__(self, origem, destino, peso, tipo):
    self.origem = origem;
    self.destino = destino;
    self.peso = peso;
    self.tipo = tipo;

def encontrar_AGM(arestas, n):
  agm, subconjuntos = [], [];
  
  # Função auxiliar para encontrar o subconjunto de um elemento 'i'
  def encontrar(subconjuntos, i):
    if subconjuntos[i].pai != i:
      subconjuntos[i].pai = encontrar(subconjuntos, subconjuntos[i].pai);
    return subconjuntos[i].pai;

  # Função auxiliar para realizar a união de dois subconjuntos x e y
  def unir(subconjuntos, x, y):
    raiz_x = encontrar(subconjuntos, x);
    raiz_y = encontrar(subconjuntos, y);
    
    if subconjuntos[raiz_x].classificacao < subconjuntos[raiz_y].classificacao:
      subconjuntos[raiz_x].pai = raiz_y;
    elif subconjuntos[raiz_x].classificacao > subconjuntos[raiz_y].classificacao:
      subconjuntos[raiz_y].pai = raiz_x;
    else:
      subconjuntos[raiz_y].pai = raiz_x;
      subconjuntos[raiz_x].classificacao += 1;
  
  # Ordeno as arestas primeiro por tipo (0 - ferrovia | 1 - rodovia), depois por peso (custo)
  arestas.sort(key=lambda x: (x.tipo, x.peso));
  # print("Arestas ordenadas:");
  # for ar in arestas:
  #   print(ar.origem, ar.destino, ar.peso, ar.tipo);
  
  # Inicializa os subconjuntos
  for i in range(n):
    subconjuntos.append(Subconjunto(i, 0));
  
  i, peso = 0, 0; # Índice para percorrer as arestas
  while len(agm) < n - 1 and i < len(arestas):
    aresta = arestas[i];
    
    raiz_origem = encontrar(subconjuntos, aresta.origem);
    raiz_destino = encontrar(subconjuntos, aresta.destino);
    
    if raiz_origem != raiz_destino:
      peso += aresta.peso;
      agm.append(aresta);
      unir(subconjuntos, raiz_origem, raiz_destino);
    
    i += 1;
  
  print(peso);

# ferrovia = 0;
# rodovia = 1;
# 3 3 2 # cidades | ferrovias | rodovias

# arestas = [ 
# Aresta(1, 2, 1000, 0), # 0
# Aresta(1, 3, 1000, 0), # 0
# Aresta(2, 3, 900, 0), # 0
# Aresta(1, 3, 800, 1), # 1
# Aresta(2, 3, 700, 1), # 1
# ]
# encontrar_AGM(arestas, 4); # arestas | N + 1

N, F, R = map(int, input().split());

arestas = [];

# cidade A - cidade B - custo
for _ in range(F): # ferrovias
  A, B, C = map(int, input().split());
  arestas.append(Aresta(A, B, C, 0));

for _ in range(R): # rodovias
  I, J, K = map(int, input().split());
  arestas.append(Aresta(I, J, K, 1));

encontrar_AGM(arestas, N+1);