import java.util.Locale;
import java.util.Scanner;

public class Bee1065 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int count = 0;
		int x;
		
		for (int i = 0; i<5; i++) {
			x = ler.nextInt();
			if (x % 2 == 0) 
				count++;
		}		
		
		System.out.println(count + " valores pares");
		
		ler.close();
	}
}
