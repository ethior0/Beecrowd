import java.util.Scanner;
import java.util.Locale;

public class Bee1015 {

	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double x1, y1, y2, x2, distance;
		
		x1 = ler.nextDouble();
		y1 = ler.nextDouble();
		x2 = ler.nextDouble();
		y2 = ler.nextDouble();
		
		distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
				
		System.out.format("%.4f\n", distance);
		ler.close();
	}
}
