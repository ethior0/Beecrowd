import java.util.Locale;
import java.util.Scanner;

public class Bee1133 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int max = 0, min = 0;
		
		int x = ler.nextInt();
		int y = ler.nextInt();
		
		if (x>y){
			max = x;
			min = y;
		} else {
			max = y;
			min = x;
		}
		
		for (int i = min+1; i<max; i++) {
			if (i%5==2 || i%5==3) {
				System.out.println(i);
			}
		}
		
		ler.close();
	}
}
