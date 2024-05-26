import java.util.Locale;
import java.util.Scanner;

public class Bee1149 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int sum = 0;
		
		int a = ler.nextInt();
		int n = ler.nextInt();
		
		if (n<=0) {
			
			for (;;) {
				n = ler.nextInt();
				if (n>0) {
					break;
				}
			}
		}
		
		for (int i = 0; i<=n-1; i++) {
			sum += a+i; 
		}
		
		System.out.println(sum);
		
		ler.close();
	}
}
