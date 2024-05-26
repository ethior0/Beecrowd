import java.util.Locale;
import java.util.Scanner;

public class Bee1118 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double n1, n2, m;
		int x = 0;
		
		do {
			
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
		
		//novo calculo?
		
		System.out.println("novo calculo (1-sim 2-nao)");
		x = ler.nextInt();
		
		// loop do 1-S 2-N
		
			if (x<1 || x>2) {
				for (;;) {
					System.out.println("novo calculo (1-sim 2-nao)");
					x = ler.nextInt();
					if (x==1 || x==2) {
						break;
					}
				}
			}
		
		
		} while (x==1);
		
		
		ler.close();
	}
}
