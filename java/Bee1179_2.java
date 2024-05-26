import java.util.Scanner;

public class Bee1179_2 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int pp = 0, im = 0, p1 = 0, p2 = 0;
		int n[] = new int[15];
		
		for (int i = 0; i < n.length; i++) {
			n[i] = ler.nextInt();
			
			if (n[i]%2 == 0) {
				pp++;
			} else {
				im++;
			}
		}
		
		int cc1 = 0, cc2 = 0;
		
		int vPar[] = new int[pp];
		for (int value: n) {
			if (value%2 == 0) {
				vPar[cc1] = value;
				System.out.println("par["+cc1+"] = "+vPar[cc1]);
				if (cc1>=4) break;
				cc1++;
			}
		
		int vImpar[] = new int[im];
		for (int value2: n) {
			if (value2%2 != 0) {
				vImpar[cc2] = value2;
				System.out.println("impar["+cc2+"] = "+vImpar[cc2]);
				if (cc2>=4) break;
				cc2++;
			}
		cc2 = 5;
		} for (int value2: n) {
			if (value2%2 != 0) {
				vImpar[cc2] = value2;
				System.out.println("impar["+p1+"] = "+vImpar[cc2]);
				p1++;
				cc2++;
			}
		} 
		cc1 = 5;
		} for (int value: n) {
			if (value%2 == 0) {
				vPar[cc1] = value;
				System.out.println("par["+p2+"] = "+vPar[cc1]);
				p2++;
				cc1++;
			}
		}
		

		ler.close();
	}
}
