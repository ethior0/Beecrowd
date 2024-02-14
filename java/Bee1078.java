import java.util.Locale;
import java.util.Scanner;

public class Bee1078 {

	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int n = ler.nextInt();
		
		for (int i = 1; i<=10; i++) {
			
			int multi = i*n;
			System.out.println(i+" x "+n+ " = "+multi);
			
		}
		
		ler.close();
	}
	
}
