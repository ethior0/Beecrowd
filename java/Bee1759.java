import java.util.Scanner;

public class Bee1759 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int N = ler.nextInt();
		
		for (int i = 0; i < N; i++) {
			System.out.print(i == N - 1 ? "Ho!" : "Ho ");
		}
		System.out.println();
		
		ler.close();
	}
}
