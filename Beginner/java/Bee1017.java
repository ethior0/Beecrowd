import java.util.Scanner;
import java.util.Locale;

public class Bee1017 {
	
	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int hour, speed;
		double distance, fuel;
		
		hour = ler.nextInt();
		speed = ler.nextInt();
		
		distance = speed*hour;
		
		fuel = distance/12;
		
		System.out.format("%.3f\n", fuel);
		ler.close();
	}
}