import java.util.Scanner;

public class Bee1165 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int num = 1, cc, cc2;
		
		int n = ler.nextInt();
		
		for (int i = 0; i<n; i++) {
			
			int x = ler.nextInt();
			
			cc = 0;
			cc2 = 2;
			num = 1;
			
			while (cc<2) {
				if (x/num==1) {
					cc++;
					if (x==1) {
						System.out.println("1 nao eh primo");
						break;
					}
				} else if (x/num==x) {
					cc++;
				} else if (x%num==0) {
					cc2++;
					break;
				}
				
				num++;
			}
			
			if (cc==2) {
				System.out.println(x + " eh primo");
			} else if (cc2>2) {
				System.out.println(x + " nao eh primo");
			} 
		}
		
		
		ler.close();
	}
}
