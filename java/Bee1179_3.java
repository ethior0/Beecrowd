import java.util.Scanner;

public class Bee1179_3 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int p = 0, i = 0;
		int n[] = new int[15];
		
		for (int f = 0; f < n.length; f++) {
			n[f] = ler.nextInt();
			
			if (n[f]%2 == 0) {
				p++;
			} else {
				i++;
			}
		}
		
		int par[] = new int[p];
		int impar[] = new int[i];
		
		for (int q = 0; q < n.length; q++) {
			
			if (n[q]%2 == 0) {
				par[q] = n[q];
			} else {
				impar[q] = n[q];
			}
		}
		

		ler.close();
	}
}
