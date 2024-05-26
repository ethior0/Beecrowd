import math;

def doOperation(N1, D1, op, N2, D2):
  if op == "+":
    return [((N1 * D2) + (N2 * D1)), (D1 * D2)];
  elif op == "-":
    return [((N1 * D2) - (N2 * D1)), (D1 * D2)];
  elif op == "*":
    return [(N1 * N2),  (D1 * D2)];
  else:
    return [(N1 * D2), (D1 * N2)];

N = int(input());

for i in range(N):
  line = input().split(" ");
  N1, D1, op, N2, D2 = line[0], line[2], line[3], line[4], line[6];
  res = doOperation(int(N1), int(D1), op, int(N2), int(D2));

  resN, resD = int(res[0]), int(res[1]);
  gcd = math.gcd(resN, resD);

  print(f"{resN}/{resD} = {int(resN / gcd)}/{int(resD / gcd)}");