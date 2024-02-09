import java.util.Locale;
import java.util.Scanner;

public class Bee1079 {

	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int n = ler.nextInt();
		
		for (int i = 0; i<n; i++) {
			double a = ler.nextDouble();
			double b = ler.nextDouble();
			double c = ler.nextDouble();
			
			double media = (a*2+b*3+c*5)/10;
			
			System.out.printf("%.1f\n", media);
		}
		
		ler.close();
	}
	
}
