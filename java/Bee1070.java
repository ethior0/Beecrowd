import java.util.Locale;
import java.util.Scanner;

public class Bee1070 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		short x = ler.nextShort();
		int y;
		
		y = x + 12;
		
		for (int i = x; i<y; i++) {
			
			if (i%2 != 0) {
				System.out.println(i);	
			}
		}	
		
		ler.close();
	}
}
