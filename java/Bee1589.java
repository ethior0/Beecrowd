import java.util.Scanner;

public class Bee1589 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int T = ler.nextInt();
		
		for (int i = 0; i < T; i++) {
			int R1 = ler.nextInt(), R2 = ler.nextInt();
			System.out.println(R1 + R2);
		}
		
		ler.close();
	}
}
