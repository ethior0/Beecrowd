import java.util.Scanner;

public class Bee1175 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int p = 0;
		
		int n[] = new int[20];
		
		for (int i = 0; i < n.length; i++) {
			n[i] = ler.nextInt();
		}
		
		for (int j = 19; j >= 0; j--) {
			System.out.println("N["+p+"] = "+n[j]);
			p++;
			
		}
		
		ler.close();
	}
}
