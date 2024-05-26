import java.util.Scanner;

public class Bee1557 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int N = ler.nextInt();
		
		while (N != 0) {
			
			int aux = 0, aux2 = 1;
			int matriz[][] = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				aux = aux2;
				for (int j = 0; j < N; j++) {
					matriz[i][j] = aux;
					aux *= 2;
					if (j == 1) aux2 = matriz[i][j];
				}
			}
			
			int lengS = String.valueOf((int) aux/2).length();
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					String line = String.format("%" + lengS + "d", matriz[i][j]);
					System.out.print(j == 0 ? line : " " + line);
				}
				System.out.println();
			}
			System.out.println();
			
			N = ler.nextInt();
		}
		
		ler.close();
	}
}
