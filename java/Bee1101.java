import java.util.Locale;
import java.util.Scanner;

public class Bee1101 {

	public static void main (String[] args) {
	
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
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
			System.out.print("Sum="+soma);
		} else {
			System.out.println("");
		}
		
		
		ler.close();
	}
}
