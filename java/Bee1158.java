import java.util.Locale;
import java.util.Scanner;

public class Bee1158 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int soma = 0;
		int n = ler.nextInt();
		
		for (int i = 0; i<n; i++) {
			
			int x = ler.nextInt();
			int y = ler.nextInt();

			
			if (x%2==0) { 
				for (int j = x+1; j<x+(2*y); j++) {
					
					if (j%2!=0) {
						soma += j;
					}
				}
				
				System.out.println(soma);
				soma = 0;
				
			} else { 
				for (int f = x; f<x+(2*y); f++) {
					
					if (f%2!=0) {
						soma += f;
					}
				}
				
				System.out.println(soma);
				soma = 0;
			
			} 
		}
		
		ler.close();
	}
}
