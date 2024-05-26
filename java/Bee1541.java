import java.util.Scanner;

public class Bee1541 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int A = ler.nextInt();
		int B = ler.nextInt();
		int C = ler.nextInt();
		
		while (A != 0) {
			double aux = (A * B * 100) / C;
			System.out.println( (int) Math.sqrt(aux) );
			
			A = ler.nextInt();
			if (A == 0) break;
			B = ler.nextInt();
			C = ler.nextInt();
		}
		
		ler.close();
	}
}
