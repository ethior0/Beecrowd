package top10packages.sim;

import java.util.Locale;
import java.util.Scanner;

public class Bee1099 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
	
		int x, y, n, soma = 0;
		
		n = ler.nextInt();
		
		for (int i = 0; i<n; i++) {
			x = ler.nextInt();
			y = ler.nextInt();
			
			soma = 0;
			
			if (x>y) {
				for (int d = (y+1); d < x; d++) {
					if (d%2!=0) {
						soma += d;
					}
				}
				System.out.println(soma);
			} 
			
			else if (x<y) {
				for (int f = (x+1); f < y; f++) {
					if (f%2!=0) {
						soma += f;
					}
				}
				System.out.println(soma);
			} 
			
			else if (x==y) {
				System.out.println(0);
			}
		}
		
		ler.close();
	}
}
