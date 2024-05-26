import java.util.Scanner;

public class Bee1564 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		while (ler.hasNext()) {
			int N = ler.nextInt();
			System.out.println(N == 0 ? "vai ter copa!" : "vai ter duas!");
		}
		
		ler.close();
	}
}
