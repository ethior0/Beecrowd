def bubble_sort(items):
  for i in range(len(items)):
    already_sorted = True;
    for j in range(len(items) - i - 1):
      if len(items[j]) < len(items[j + 1]):
        items[j], items[j + 1] = items[j + 1], items[j];
        already_sorted = False;
    if already_sorted:
      break;

N = int(input());

for _ in range(N):
  lista = list(input().split());
  bubble_sort(lista);
  print(" ".join(lista));