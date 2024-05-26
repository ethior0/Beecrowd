import java.util.Scanner;

public class Bee1173 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int n[] = new int[10];
		
		int in = ler.nextInt();
		
		n[0] = in;
		n[1] = n[0]*2;
		n[2] = n[1]*2;
		n[3] = n[2]*2;
		n[4] = n[3]*2;
		n[5] = n[4]*2;
		n[6] = n[5]*2;
		n[7] = n[6]*2;
		n[8] = n[7]*2;
		n[9] = n[8]*2;
		
		for (int i = 0; i < n.length; i++) {
			System.out.println("N["+i+"] = "+n[i]);
		}
		
		ler.close();
	}
}
