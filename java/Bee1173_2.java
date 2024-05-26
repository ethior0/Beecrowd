import java.util.Scanner;

public class Bee1173_2 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int n[] = new int[10];
		
		int in = ler.nextInt();
		
		for (int i = 0; i < n.length; i++) {
			
			n[i] = in;
			in *= 2;
			System.out.println("N["+i+"] = "+n[i]);
		}
		
		ler.close();
	}
}
