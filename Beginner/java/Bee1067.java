import java.util.Locale;
import java.util.Scanner;

public class Bee1067 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		short x = ler.nextShort();
		
		for (int i = 1; i<=x; i++) {
			
			if (i%2 != 0) {
				System.out.println(i);	
			}
		}	
		
		ler.close();
	}
}
