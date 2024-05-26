import java.util.Locale;
import java.util.Scanner;

public class Bee1150 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int sum = 0, cc = 0;
		
		int x = ler.nextInt();
		int z = ler.nextInt();
		
		if (x>z) {
			for (;;) {
				z = ler.nextInt();
				if (z>x) {
					break;
				}
			}
		}
		
		for (int i = x; i<z; i++) {
			
			sum += i;
			cc++;
			if (sum>z) {
				break;
			}
		}
		
		System.out.println(cc);
		
		ler.close();
	}
}
