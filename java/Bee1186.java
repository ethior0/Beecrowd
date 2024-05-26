import java.util.Locale;
import java.util.Scanner;

public class Bee1186 {
	
	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double soma = 0;
		int diag = 11;
		
		String o = ler.next();
		
		double n[] = new double [12];
		
		for (int i = 0; i<12; i++) {
			for (int j = 0; j<12; j++) {
				n[i] = ler.nextDouble();
				if (j > diag) {
					soma += n[i];
				}
			}
			diag--;
		}
		
		if (o.equalsIgnoreCase("S") ) {
			System.out.printf("%.1f\n", soma);
		} else if (o.equalsIgnoreCase("M")) {
			System.out.printf("%.1f\n", soma/66);
		}
		
		ler.close();
	}
}
