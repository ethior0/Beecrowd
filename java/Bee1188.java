import java.util.Locale;
import java.util.Scanner;

public class Bee1188 {
	
	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double soma = 0;
		int diag = 0;
		int diag2 = 11;
		
		String o = ler.next();
		
		double n[] = new double [12];
		
		for (int i = 0; i<12; i++) {
			for (int j = 0; j<12; j++) {
				n[i] = ler.nextDouble();
				if (j < diag && j > diag2) {
					soma += n[i];
				}
			}
			diag++;
			diag2--;
		}
		
		/* esse código foi poggers
		 * era 3 AM e eu fiquei uns 40 min
		 * mudando tudo, quando eu só 
		 * precisava dormir ou trocar 2 sinais
		 * rsrsrs
		 */
		
		if (o.equalsIgnoreCase("S") ) {
			System.out.printf("%.1f\n", soma);
		} else if (o.equalsIgnoreCase("M")) {
			System.out.printf("%.1f\n", soma/30);
		}
		
		ler.close();
	}
}
