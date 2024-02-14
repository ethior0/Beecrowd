import java.util.Scanner;
import java.util.Locale;

public class Bee1020 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int day, month, year;
		
		day = ler.nextInt();
		
		year = day/365;
		
		day = day % 365;
		
		month = day/30;
		
		day = day % 30;
		
		System.out.println(year+" ano(s)");
		System.out.println(month+" mes(es)");
		System.out.println(day+" dia(s)");
		ler.close();
	}
}
