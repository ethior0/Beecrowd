import java.util.Scanner;

public class Bee1004 {
	public static void main (String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int a, b, PROD;
		
		a = ler.nextInt();
		b = ler.nextInt();
		
		PROD = a*b;
		
		System.out.println("PROD = "+PROD);
		ler.close();
		
	}		
}
