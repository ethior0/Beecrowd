import java.util.Locale;
import java.util.Scanner;

public class Bee1174 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double a[] = new double[100];
		
		for (int i = 0; i < a.length; i++) {
			a[i] = ler.nextDouble();
		}
		
		for (int j = 0; j < a.length; j++) {
			if (a[j] <= 10) {
				System.out.printf("A[%d] = %.1f\n", j, a[j]);
			}
		}
		
		ler.close();
	}
}
