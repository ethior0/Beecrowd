import math;

x1, y1 = map(float, input().split(" "));
x2, y2 = map(float, input().split(" "));
formula = math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2);
distance = math.sqrt(formula);

print(f"{distance:.4f}");
