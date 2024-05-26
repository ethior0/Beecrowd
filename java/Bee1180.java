import java.util.Scanner;

public class Bee1180 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int x = ler.nextInt();
		int n[] = new int[x];
		int menor = 0, pos = 0;
		
		for (int i = 0; i < x; i++) {
			n[i] = ler.nextInt();
			if (i == 1) {
				menor = Math.min(n[i], n[i-1]);
			} else {
				menor = Math.min(menor, n[i]);
			}
		}
		System.out.println("Menor valor: "+menor);
		
		for (int value: n) {
			if (menor == value) {
				break;
			} else {
				pos++;
			}
		}
		System.out.println("Posicao: "+pos);
		
		ler.close();
	}
}
