import java.util.Locale;
import java.util.Scanner;

public class Bee1117 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double n1, n2, m;
		
		n1 = ler.nextDouble();
		if (n1<0 || n1>10) {
			for (;;) {
				System.out.println("nota invalida");
				n1 = ler.nextDouble();
				if (n1>=0 && n1<=10) {
					break;
				}
			}
		}
		
		n2 = ler.nextDouble();
		if (n2<0 || n2>10) {
			for (;;) {
				System.out.println("nota invalida");
				n2 = ler.nextDouble();
				if (n2>=0 && n2<=10) {
					break;
				}
			}
		}
		
		m = (n1+n2)/2;
		System.out.printf("media = %.2f\n", m);
		
		ler.close();
	}
}
