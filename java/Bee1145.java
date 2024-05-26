import java.util.Locale;
import java.util.Scanner;

public class Bee1145 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int cc = 0;
		
		int x = ler.nextInt();
		int y = ler.nextInt();

		for (int i = 1; i<=y; i++) {
			
			System.out.print(i+" ");
			
			cc++;
			
			if (cc==x) {
				System.out.println("");
				cc = 0;
			}
		}
		
		ler.close();
	}
}
