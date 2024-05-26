import java.util.Locale;
import java.util.Scanner;

public class Bee1160_3 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int pb, pa, ano;
		double g1, g2;
		
		int t = ler.nextInt();
		
		for (int i = 0; i < t; i++) {
			
			ano = 0;
			
			pa = ler.nextInt();
			pb = ler.nextInt();
			g1 = ler.nextDouble();
			g2 = ler.nextDouble();
			
			while (pb>=pa) {
				pa += (pa*g1)/100; // pa = pa + (pa*g1) / 100
				pb += (pb*g2)/100; // pb = pb + (pb*g2) / 100
				ano++;
				if (ano>100) {
					break;
				} 
			}
			
			if (ano>100) {
				System.out.println("Mais de 1 seculo.");
			} else {
				System.out.println(ano+" anos.");
			}
			
		}
		
		ler.close();
	}
}
