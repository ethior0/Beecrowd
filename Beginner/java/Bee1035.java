import java.util.Scanner;
import java.util.Locale;

public class Bee1035 {
	
	public static void main (String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int A = ler.nextInt();
		int B = ler.nextInt();
		int C = ler.nextInt();
		int D = ler.nextInt();
		
		if (B>C && D>A && (C+D)>(A+B) && C>0 && D>0 && A%2==0) {
			System.out.println("Valores aceitos");
		} else {
			System.out.println("Valores nao aceitos");
		}
		
		ler.close();	
	}
}
