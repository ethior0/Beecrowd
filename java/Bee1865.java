import java.util.Scanner;

public class Bee1865 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int C = ler.nextInt();
		
		for (int i = 0; i < C; i++) {
			String nome = ler.next();
			int forca = ler.nextInt();
			System.out.println(nome.equals("Thor") ? "Y" : "N");
		}
		
		ler.close();
	}
}
