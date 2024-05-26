import java.util.Scanner;

public class Bee1179_4 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int par = 0, impar = 0, cc = 0;
		int n[] = new int[15];
		
		for (int i = 0; i < n.length; i++) {
			n[i] = ler.nextInt();
		}
		
		for (int value: n) {
			if (value%2 == 0) {
				System.out.println("par["+par+"] = "+value);
				par++;
				if (par==5) {
					break;
				}
			} 
		}

		for (int value2: n) {
			if (value2%2 != 0) {
				System.out.println("impar["+impar+"] = "+value2);
				impar++;
				if (impar==5) impar = 0;
			}
		}
		
		for (int value: n) {
			if (value%2 == 0) {
				if (par>9) {
					System.out.println("par["+cc+"] = "+value);
					cc++;
					if (cc==5) cc = 0;
				}
				par++;
				
			} 
		}
		
		ler.close();
	}
}
