A, B, C = map(float, input().split(" "));
areaTri = A * C / 2;
areaCir = 3.14159 * pow(C, 2);
areaTra = (A + B) * C / 2;
areaSqu = B * B;
areaRec = A * B;

print(f"TRIANGULO: {areaTri:.3f}");
print(f"CIRCULO: {areaCir:.3f}");
print(f"TRAPEZIO: {areaTra:.3f}");
print(f"QUADRADO: {areaSqu:.3f}");
print(f"RETANGULO: {areaRec:.3f}");