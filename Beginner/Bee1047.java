import java.util.Scanner;
import java.util.Locale;

public class Bee1047 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int h1, m1, h2, m2, hm1, hm2, h24, resultado=0; 
			
		h1 = ler.nextInt();
		m1 = ler.nextInt();
		h2 = ler.nextInt();
		m2 = ler.nextInt();
		hm1 = (h1 * 60) + m1;
		hm2 = (h2 *60) + m2;
		h24 = 24*60;
		
		if (hm2 > hm1) {
			resultado = hm2 - hm1;
			System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", (resultado / 60), (resultado % 60));
		}
		
		else if (hm1 > hm2) {
			resultado = (h24 - hm1) + hm2;
			System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", (resultado / 60), (resultado % 60));
		}
		
		else {
			System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", 24, 0);
		}
		
		ler.close();
	}
}
