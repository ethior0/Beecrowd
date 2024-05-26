import java.util.Locale;
import java.util.Scanner;

public class Bee1146 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		for (;;) {
			int x = ler.nextInt();
			
			for (int i = 1; i<=x; i++) {
				
				if (i == x) {
					System.out.print(i+"\n");
				} else {
					System.out.print(i + " ");
				}
			}
			
			if (x==0) {
				break;
			}
		}
		
		
		ler.close();
	}
}
