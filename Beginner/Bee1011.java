import java.util.Locale;
import java.util.Scanner;

public class Bee1011 {
	
	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner (System.in);
		
		double radius, VOLUME;
		
		radius = ler.nextDouble();
		
		VOLUME = (4.0/3)*3.14159*(radius*radius*radius);
		
		System.out.format("VOLUME = %.3f\n", VOLUME);
		ler.close();		
	}
}
