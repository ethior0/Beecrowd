import java.util.Scanner;
import java.util.Locale;

public class Bee1014 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int X;
		double Y, consumo;
		
		X = ler.nextInt();
		Y = ler.nextDouble();
		
		consumo = X/Y;
		
		System.out.format("%.3f km/l%n", consumo);
		ler.close();
	}

}
