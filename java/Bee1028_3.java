import java.util.Locale;
import java.util.Scanner;

public class Bee1028_3 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int a, b, quantidade, mdc = 1, resto;
		
		quantidade = ler.nextInt();
		
		for (int i=0; i<quantidade; i++) {
			a = ler.nextInt();
			b = ler.nextInt();
			
			if (a>b) {
				do {
					resto = a % b;
					a = b;
					b = resto;
				} while (resto != 0);
				mdc = a;
			} else {
				do {
					resto = b % a;
					b = a;
					a = resto;
				} while (resto!=0);
				mdc = b;
			} 
			
			System.out.println(mdc);
			
		}
				
		ler.close();
	}
	
}
