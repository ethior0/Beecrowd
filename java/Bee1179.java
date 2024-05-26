import java.util.Scanner;

public class Bee1179 {

	public static void main (String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int cc = 0, c = 0, cc2 = 0, c2 = 0;
		
		int n[] = new int[15];
		int d[] = new int[5];
		
		for (int i = 0; i < n.length; i++) {
			n[i] = ler.nextInt();
		}
		
		for (int value: n) {
			if (value%2 == 0 && cc<5) {
				d[cc] = value; 
				System.out.println("par["+cc+"] = "+value);
				cc++;
			} 
		}
		
		for (int value2: n) {
			if (value2%2 != 0 && c<5){
				d[c] = value2;
				System.out.println("impar["+c+"] = "+value2);
				c++;
				}
			}
		
		for (int i = 10; i <15 ; i++) {
			if (n[i]%2 != 0){
				System.out.println("impar["+cc2+"] = "+n[i]);
				cc2++;
			}
		} 
		
		for (int i = 10; i <15 ; i++) {
			if (n[i]%2 == 0) {
				System.out.println("par["+c2+"] = "+n[i]);
				c2++;
			}
		}
		
		ler.close();
	}
}
