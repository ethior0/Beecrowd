import java.util.Locale;
import java.util.Scanner;

public class Bee1154 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int cc = 1;
		double total = 0, res;
		
		int d = ler.nextInt();
		total += d;
		
		if (d>0) {
			for (;;) {
				d = ler.nextInt();
				if (d<0) {
					break;
				}
				total += d;
				cc++;
			}
		} 
		
		res = (double) total/cc;
		
		System.out.printf("%.2f\n", res);
		
		ler.close();
	}
}
