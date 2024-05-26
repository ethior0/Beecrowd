import java.util.Locale;
import java.util.Scanner;

public class Bee1160_2 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int ano, pA, pB;
		double g1, g2;
		
		int t = ler.nextInt();
		
		for (int i = 0; i < t; i++) {
			
			ano = 0;
			
			pA = ler.nextInt();
			pB = ler.nextInt();
			g1 = ler.nextDouble();
			g2 = ler.nextDouble();
			
			while (pB>=pA) {
				pA += (pA * g1) / 100;
				pB += (pB * g2) / 100;
				ano++;
				
				if (ano > 100) {
					break;
				}
			}
			
			if (ano > 100) {
				System.out.println("Mais de 1 seculo.");
			} else {
				System.out.println(ano + " anos.");
			}
			
		}
		
		
		ler.close();
	}
}
