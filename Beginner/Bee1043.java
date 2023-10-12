import java.util.Scanner;
import java.util.Locale;

public class Bee1043 {
	
	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double A, B, C, perimeter, area;
		
		A = ler.nextDouble();
		B = ler.nextDouble();
		C = ler.nextDouble();

		perimeter = A + B + C;
		area = ((A+B)*C)/2;
		
		if (A<(B+C) && B<(A+C) && C<(A+B)) {
			System.out.printf("Perimetro = %.1f\n", perimeter);
		} if (!(A < (B + C) && B < (A + C) && C < (A + B))) {
			System.out.printf("Area = %.1f\n", area);
		}
		
		ler.close();
	}
}
