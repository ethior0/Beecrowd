import java.util.Scanner;

public class Bee1159 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int cc = 1, soma = 0;
		
		for (;;) {
			
			int x = ler.nextInt();
			
			if (x==0) {
				break;
			}
			
			if (x%2==0) {
				for (int i = x; i<x*5; i++) {
					
					if (i%2==0) {
						soma += i;
						if (cc==5) {
							break;
						}
						cc++;
					}
				}
				
				System.out.println(soma);
				soma = 0;
				cc = 1;
				
			} else if (x%2!=0) {
				for (int f = x+1; f<x*5; f++) {
					
					if (f%2==0) {
						soma += f;
						if (cc==5) {
							break;
						}
						cc++;
					}
				}
				
				System.out.println(soma);
				soma = 0;
				cc = 1;
				
			}
		}
		
		ler.close();
	}
}
