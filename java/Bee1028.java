import java.util.Locale;
import java.util.Scanner;

public class Bee1028 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int count = ler.nextInt();
		
		for (int i = 0; i<count; i++) {
			int deck1 = ler.nextInt();
			int deck2 = ler.nextInt();
			
			for (int f = 2000; f>=1; f--) {
				if (deck1%f == 0 && deck2%f == 0) {
					System.out.println(f);
					break;
				}
			}
		} 
		
		ler.close();
	}
	
}
