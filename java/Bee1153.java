import java.util.Locale;
import java.util.Scanner;

public class Bee1153 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int f = 1;
		
		int n = ler.nextInt();
		
		for (int i = n; i>1; i--) {	
			f *= i; 
		}
		
		System.out.println(f);
		
		
		ler.close();
	}
}
