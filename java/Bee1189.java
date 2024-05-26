import java.util.Locale;
import java.util.Scanner;

public class Bee1189 {
	
	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double soma = 0;
		int diag = 0;
		int diag2 = 6;
//		int cc = 0; // contador da soma
		int cc2 = 0;
		
		String o = ler.next();
		
		double n[] = new double [12];
		
		for (int i = 0; i<12; i++) {
			for (int j = 0; j<12; j++) {
				n[i] = ler.nextDouble();
				if (j < diag && j < diag2) {
					soma += n[i];
//					cc++;
				}
			}
			if (diag==5) {
				diag = 5;
				cc2++;
				if (cc2>=1) {
					/* podia ser diferente tipo cc2>1 e diag2 = 5, 
					 * dá no mesmo, mas ja que foi a forma que eu achei inicialmente
					 * preferi mantê-la
					 */
					diag2--;
				}
			} else if (diag<5) {
				diag++; // 5				
			} 
		}
		
		/*System.out.println(cc);
		* só pra mostrar quantas vezes ele somou,
		* que no caso tem que ser 30
		*/
		
		if (o.equalsIgnoreCase("S") ) {
			System.out.printf("%.1f\n", soma);
		} else if (o.equalsIgnoreCase("M")) {
			System.out.printf("%.1f\n", soma/30);
		}
		
		ler.close();
	}
}
