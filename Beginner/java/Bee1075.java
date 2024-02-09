import java.util.Locale;
import java.util.Scanner;

public class Bee1075 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int n = ler.nextInt();
		
		for (int i=0; i<10000; i++) {
			int resto = i%n;
				
			if (resto == 2) {
				System.out.println(i);
			}
		}
	
		ler.close();
	}
	
}
