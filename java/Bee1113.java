import java.util.Locale;
import java.util.Scanner;

public class Bee1113 {

	public static void main (String[] args) {
	
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		for(;;) {
			
			int num1 = ler.nextInt();
			int num2 = ler.nextInt();
			
			if (num1>num2) {
				System.out.println("Decrescente");
			} else if (num1<num2) {
				System.out.println("Crescente");
			} else {
				break;
			}
			
			ler.close();
		}
	}
}
