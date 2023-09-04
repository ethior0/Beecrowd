import java.util.Scanner;
public class Soma {
	public static void main (String[] args) {
	Scanner ler = new Scanner(System.in);
	
		int A, B, X;
		
		A = ler.nextInt();
		B = ler.nextInt();
		
		X = A+B;
		
		System.out.println("X = "+X);
		ler.close();
		
	}
}
