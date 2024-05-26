import java.util.Locale;
import java.util.Scanner;

public class Bee1101_2 {

	public static void main (String[] args) {
	
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
			
		for (int z = 0; z < 3; z++) {
			
			int soma = 0;
			
			int m = ler.nextInt();
			int n = ler.nextInt();	
			
			int max = Math.max(m, n);
			int min = Math.min(m, n); 
			
			if (m>0 && n>0) {
				
				for (int i = min; i<=max; i++) {
					System.out.print(i+" ");
					soma += i;
				}
				System.out.printf("Sum=%d\n", soma);
			} 
		}

		ler.close();
	}
}
