import java.util.Locale;
import java.util.Scanner;

public class Bee1074 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int n = ler.nextInt();
		
		for (int i = 0; i<n; i++) {
			int x = ler.nextInt();
			if (x==0) {
				System.out.println("NULL");
			} else if (x>0 && x%2==0) {
				System.out.println("EVEN POSITIVE");
			} else if (x<0 && x%2==0) {
				System.out.println("EVEN NEGATIVE");
			} else if (x>0 && x%2!=0) {
				System.out.println("ODD POSITIVE");
			} else {
				System.out.println("ODD NEGATIVE");
			}
		}
		
		ler.close();
	}
	
}
