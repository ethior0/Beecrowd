import java.util.Locale;
import java.util.Scanner;

public class Bee1071_2 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int x = ler.nextInt();
		int y = ler.nextInt();
		int max, min;
		int soma = 0;
		
		if (x>y) {
			max = x;
			min = y;
		} else {
			max = y;
			min = x;
		}
		
		for (int i = ++min; i<max; i++) {
			if (i%2 != 0) {
				soma += i;
			}
		}
		
		System.out.println(soma);
		
		ler.close();
	}
	
}
