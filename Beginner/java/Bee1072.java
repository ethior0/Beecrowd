import java.util.Locale;
import java.util.Scanner;

public class Bee1072 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int n = ler.nextInt();
		int count1 = 0;
		int count2 = 0;
		
		for (int i = 0; i<n; i++) {
			int x = ler.nextInt();
			
			if (x>=10 && x<=20) {
				++count1;
			} else {
				++count2;
			}
		}
		
		System.out.println(count1+" in");
		System.out.println(count2+" out");
		
		ler.close();
	}
	
}