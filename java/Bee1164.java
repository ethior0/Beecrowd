import java.util.Scanner;

public class Bee1164 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int x, n;
		
		n = ler.nextInt();
		
		for (int i = 0; i<n; i++) {
			
			int e = 1;
			int tot = 0;
			
			x = ler.nextInt();
			
			while (e<=x) {
				tot += e; // total = total + e;
				if (tot>x) {
					System.out.println(x + " nao eh perfeito");
					break;
				} else if (tot==x) {
					if (x==1) {
						System.out.println(x + " nao eh perfeito");
						break;
					} else {
						System.out.println(x + " eh perfeito");
						break;
					}
				} 
				e++;
			}
		}
		
		ler.close();
	}
}
