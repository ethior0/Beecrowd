def merge_sort(lista, inicio = 0, fim = None):
  if fim is None:
    fim = len(lista);
  if (fim - inicio > 1):
    meio = (fim + inicio) // 2;
    merge_sort(lista, inicio, meio);
    merge_sort(lista, meio, fim);
    merge(lista, inicio, meio, fim);
  return lista;

def merge(lista, inicio, meio, fim):
  left = lista[inicio:meio];
  right = lista[meio:fim];
  top_left, top_right = 0, 0;
  for k in range(inicio, fim):
    if top_left >= len(left):
      lista[k] = right[top_right];
      top_right += 1;
    elif top_right >= len(right):
      lista[k] = left[top_left];
      top_left += 1;
    elif left[top_left] > right[top_right]:
      lista[k] = left[top_left];
      top_left += 1;
    else:
      lista[k] = right[top_right];
      top_right += 1;

N = int(input());

for _ in range(N): 
  M = int(input());
  
  notas = list(map(int, input().split()));
  notasSorted = merge_sort(notas.copy()); 

  diferencas = sum(1 for x, y in zip(notas, notasSorted) if x != y);
  print(M - diferencas);