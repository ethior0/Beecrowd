import java.util.Scanner;
import java.util.Locale;

public class Bee1019 {
	
	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int N, minutes, hours;
		
		N = ler.nextInt();
		
		minutes = N/60;
		
		N = (N % 60);
		
		hours = minutes/60;
		
		minutes = (minutes % 60);
		
		System.out.println(hours+":"+minutes+":"+N);
		ler.close();
	}
}
