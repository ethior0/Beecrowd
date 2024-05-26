import java.util.Scanner;

public class Bee1177 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
	
		int cc = 0;
		
		
		int n[] = new int[1000];
		
		int t = ler.nextInt();
		
		for (int i = 0; i < n.length; i++) {

			System.out.println("N["+i+"] = "+cc);
			cc++;
			
			if (cc>=t) {
				cc = 0;
			}
			
		}
		
		ler.close();
	}
}
