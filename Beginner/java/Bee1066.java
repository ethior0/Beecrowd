import java.util.Locale;
import java.util.Scanner;

public class Bee1066 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int count1 = 0, count2 = 0, count3 = 0, count4 = 0;
		int x;
		
		for (int i = 0; i<5; i++) {
			x = ler.nextInt();
			if (x % 2 == 0) {
				count1++;
			} 
			if (x % 2 != 0) {
				count2++;
			}
			if (x>0) {
				count3++;
			}
			if (x<0) {
				count4++;
			}
		}
		
		System.out.println(count1 + " valor(es) par(es)");
		System.out.println(count2 + " valor(es) impar(es)");
		System.out.println(count3 + " valor(es) positivo(s)");
		System.out.println(count4 + " valor(es) negativo(s)");
	
		ler.close();
	}
}
