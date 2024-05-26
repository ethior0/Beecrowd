import java.util.Locale;
import java.util.Scanner;

public class Bee1132 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int max = 0, min = 0, soma = 0;
		
		int x = ler.nextInt();
		int y = ler.nextInt();
		
		if (x>y) {
			max = x;
			min = y;
		} else {
			max = y;
			min = x;
		} 
		
		for (int i = min; i<=max; i++) {
			if (i % 13 != 0) {
				soma += i;
			}
		}
		
		System.out.println(soma);
		
		ler.close();
	}
}
