import java.util.Locale;
import java.util.Scanner;

public class Bee1178 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double x = ler.nextDouble();
		double n[] = new double[100];
		
		for (int i = 0; i < n.length; i++) {
			n[i] = x;
			System.out.printf("N[%d] = %.4f\n", i, x);
			x = x/2;
		}
		
		ler.close();
	}
}
