import java.util.Locale;
import java.util.Scanner;

public class Bee1115 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		for (;;) {
			int x = ler.nextInt();
			int y = ler.nextInt();
			
			if (x>0 && y>0) System.out.println("primeiro");
			else if (x<0 && y>0) System.out.println("segundo");
			else if (x<0 && y<0) System.out.println("terceiro");
			else if (x>0 && y<0	) System.out.println("quarto");
			else break;
			
			ler.close();
		}
	}
}
