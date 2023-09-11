import java.util.Locale;
import java.util.Scanner;

public class Bee1012 {
	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double PI, A, B, C, triangle, circle, trapezium, square, rectangle;
		
		A = ler.nextDouble();
		B = ler.nextDouble();
		C = ler.nextDouble();
		
		PI = 3.14159;
		
		triangle = (A*C)/2.0;
		circle = PI*(C*C);
		trapezium = ((A+B)*C)/2.0;
		square = B*B;
		rectangle = A*B;
				
		System.out.format("TRIANGULO: %.3f\n", triangle);
		System.out.format("CIRCULO: %.3f\n", circle);
		System.out.format("TRAPEZIO: %.3f\n", trapezium);
		System.out.format("QUADRADO: %.3f\n", square);
		System.out.format("RETANGULO: %.3f\n", rectangle);
		ler.close();
	}
}
