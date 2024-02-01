import java.util.Scanner;
import java.util.Locale;

public class Bee1036 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double delta, r1, r2;
		
		double A = ler.nextDouble();
		double B = ler.nextDouble();
		double C = ler.nextDouble();
		
		delta = Math.pow(B, 2)-(4*A*C);
		
		r1 = (-B + Math.sqrt(delta) )/ (2 * A);
		r2 = (-B - Math.sqrt(delta) )/ (2 * A);
		
		
		if (A==0 || delta<0) {
			System.out.println("Impossivel calcular");
		} else {
			System.out.printf("R1 = %.5f\n", r1);
			System.out.printf("R2 = %.5f\n", r2);
		}
		
		
		ler.close();
	}
}
