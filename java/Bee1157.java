import java.util.Locale;
import java.util.Scanner;

public class Bee1157 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int n = ler.nextInt();
		
		for (int i = 1; i<=n; i++) {
			
			if (n%i==0) {
				System.out.println(i);
			}
			
		}
		
		ler.close();
	}
}
