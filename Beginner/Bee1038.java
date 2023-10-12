import java.util.Scanner;
import java.util.Locale;

public class Bee1038 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double value;
		
		int code = ler.nextInt();
		int amount = ler.nextInt();
		
		if (code==1) {
			value = amount*4.00;
			System.out.printf("Total: R$ %.2f\n", value);
		}
		
		if (code==2) {
			value = amount*4.50;
			System.out.printf("Total: R$ %.2f\n", value);
		}
		
		if (code==3) {
			value = amount*5.00;
			System.out.printf("Total: R$ %.2f\n", value);
		}
		
		if (code==4) {
			value = amount*2.00;
			System.out.printf("Total: R$ %.2f\n", value);
		}
		
		if (code==5) {
			value = amount*1.50;
			System.out.printf("Total: R$ %.2f\n", value);
		}
		
		ler.close();
	}
}
