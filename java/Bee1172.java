import java.util.Scanner;

public class Bee1172 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int x[] = new int[10];
		
//		x[0] = ler.nextInt();
//		x[1] = ler.nextInt();
//		x[2] = ler.nextInt();
//		x[3] = ler.nextInt();
//		x[4] = ler.nextInt();
//		x[5] = ler.nextInt();
//		x[6] = ler.nextInt();
//		x[7] = ler.nextInt();
//		x[8] = ler.nextInt();
//		x[9] = ler.nextInt();
		
		for (int i = 0; i < x.length; i++) {
			
			x[i] = ler.nextInt();
			
			if (x[i]<=0) {
				System.out.println("X["+i+"] = 1");
			} else {
				System.out.println("X["+i+"] = "+x[i]);
			}
		}
		
		ler.close();
	}
}
