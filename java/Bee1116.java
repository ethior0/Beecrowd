import java.util.Locale;
import java.util.Scanner;

public class Bee1116 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int n = ler.nextInt();
		
		for (int i = 0; i<n; i++) {
			int x = ler.nextInt();
			int y = ler.nextInt();
			
			if (y==0) {
				System.out.println("divisao impossivel");
			} else {
				double resultado = (double) x/y;
			System.out.printf("%.1f\n", resultado);
			}
		}
		
		ler.close();
	}
}
