import java.util.Locale;
import java.util.Scanner;

public class Bee1080 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int max = 0, position = 0, b = 0;
		
		for (int i = 1; i<=100; i++) {
			int a = ler.nextInt();
			
			max = Math.max(a, b);
			if (a>b) {
				b = a;
				position = i;
			} 
		}
		
		System.out.println(max);
		System.out.println(position);
		
		ler.close();
	}
}
	

// fiquei feliz fazendo esse aqui, pprt, desenrolei muito bem
