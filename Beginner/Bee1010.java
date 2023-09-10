import java.util.Locale;
import java.util.Scanner;

public class Bee1010 {
	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner (System.in);
		
		int code01, units01, code02, units02;
		double priceUnit01, priceUnit02, VALUE;
		
		code01 = ler.nextInt();
		units01 = ler.nextInt();
		priceUnit01 = ler.nextDouble();
		
		code02 = ler.nextInt();
		units02 = ler.nextInt();
		priceUnit02 = ler.nextDouble();
		
		VALUE = (units01*priceUnit01)+(units02*priceUnit02);
		
		System.out.format("VALOR A PAGAR: R$ %.2f\n", VALUE);
		ler.close();
		
	}
}
