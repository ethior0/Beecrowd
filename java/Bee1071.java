import java.util.Locale;
import java.util.Scanner;

public class Bee1071 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int x = ler.nextInt();
		int y = ler.nextInt();
		int min, max, soma = 0;
		
		if (x<y) {
			min = x;
			max = y;
		} else {
			min = y;
			max = x;
		}
		
		for (int i=min+1; i<max; i++) {
			if (i%2 != 0) {
				soma += i;
		}
	}
		
		System.out.println(soma);
		
		ler.close();
	}
}
