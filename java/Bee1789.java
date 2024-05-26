import java.util.Arrays;
import java.util.Scanner;

public class Bee1789 {

	public static void main(String[] argzs) {
		
		Scanner ler = new Scanner(System.in);
		
		while (ler.hasNext()) {
			
			int L = ler.nextInt();
			int matriz[] = new int [L];
			
			for (int i = 0; i < L; i++) {
				matriz[i] = ler.nextInt();
			}
			Arrays.sort(matriz);
			
			System.out.println(matriz[L-1] < 10 ? "1" : matriz[L-1] < 20 ? "2" : "3");
		}
		
		ler.close();
	}
}
