import java.util.Scanner;

public class Bee1176 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		long num1, num2, num3, cc = 0;
		
		int t = ler.nextInt();
		
		for (int i = 0; i < t; i++) {

			int n = ler.nextInt();
			
			if (n==0) {
				num1 = 0;
				System.out.println("Fib("+n+") = "+num1);
			} else if (n==1) {
				num1 = 1;
				System.out.println("Fib("+n+") = "+num1);
			} else if (n==2) {
				num1 = 1;
				System.out.println("Fib("+n+") = "+num1);
			} else {
				
				cc = 0;
				num1 = 0;
				num2 = 1;
				num3 = 0;
				
				while (cc<=n-1) {
					num3 = num1 + num2;
					num1 = num2;
					num2 = num3;
					cc++;
				}
				
				System.out.println("Fib("+n+") = "+num1);
			}
			
		}
		
		//while (cc<=n-1)
		
		ler.close();
	}
}
