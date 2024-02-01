import java.util.Scanner;
import java.util.Locale;

public class Bee1016 {
	
	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int km, minutes;
		
		km = ler.nextInt();
		
		minutes = km*2;
		
		System.out.println(minutes+" minutos");
		ler.close();
	}
}
