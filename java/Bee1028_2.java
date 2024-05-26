import java.util.Locale;
import java.util.Scanner;

public class Bee1028_2 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int a, b, teste, mdc = 1, resto;
		teste = ler.nextInt();
		
		
		for (int i = 0; i<teste; i++) {
			a = ler.nextInt();
			b = ler.nextInt();
			
			if (a > b) {
				do {
					resto = a % b;
					a = b;
					b = resto;
				} while (resto != 0);
				mdc = a;
			}
			else {
				do {
					resto = b % a;
					b = a;
					a = resto;
				} while (resto != 0);
				mdc = b;
			}
			System.out.println(mdc);
		} 
		
		// esse é o correto lixo horrivel q deu certo n sei pq '-'
		
		ler.close();
	}
	
}
