import java.util.Locale;
import java.util.Scanner;

public class Bee1142 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int num1 = 1, num2 = 2, num3 = 3;
		
		int n = ler.nextInt();
		
		for (int i = 0; i < n; i++) {
			System.out.println(num1+" "+num2+" "+num3+" PUM");
			num1 += 4;
			num2 += 4;
			num3 += 4;
		}
		
		ler.close();
	}
}
