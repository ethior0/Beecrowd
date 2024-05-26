import java.util.Locale;
import java.util.Scanner;

public class Bee1151 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
			
		int num1 = 0, num2 = 1, num3 = 0;
		
		int n = ler.nextInt();
		
		System.out.print(num1+" ");
		System.out.print(num2+" ");
		
		for (int i = 1; i <= n-2; i++) {

			if (i<n-2) {
				num3 = num1 + num2;
				System.out.print(num3+" ");
				num1 = num2;
				num2 = num3;
			} else {
				System.out.print(num1+num2+"\n");
			}
				
		}

		ler.close();
	}
}
