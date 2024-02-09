import java.util.Locale;
import java.util.Scanner;

public class Bee1080_2 {

	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int a[] = new int[100];
		int b = 0, max = 0, position = 0;
		
		for (int i = 0; i<a.length; i++) {
			a[i] = ler.nextInt();
			
			max = Math.max(a[i], b);
			if (a[i]>b) {
				b = a[i];
				position = i+1;
			}
		}

		System.out.println(max);
		System.out.println(position);
		
		ler.close();
	}
	
}
