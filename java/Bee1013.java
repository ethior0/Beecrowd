import java.util.Locale;
import java.util.Scanner;

public class Bee1013 {
	
	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int a, b, c, maiorAB, maiorABC;
		
		a = ler.nextInt();
		b = ler.nextInt();
		c = ler.nextInt();
		
		maiorAB = (a+b+Math.abs(a-b))/2;
		
		maiorABC = (maiorAB+c+Math.abs(maiorAB-c))/2;

		System.out.println(maiorABC+" eh o maior");
		ler.close();
	}
}
