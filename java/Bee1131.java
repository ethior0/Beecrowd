import java.util.Locale;
import java.util.Scanner;

public class Bee1131 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int grenal = 0, total = 0, gI, gG, ccI = 0, ccG = 0, ccE = 0;
		String win = "";
		
		do {
			
			gI = ler.nextInt();
			gG = ler.nextInt();
			
			if (gI>gG) {
				ccI++;
			} else if (gG>gI) {
				ccG++;
			} else {
				ccE++;
			}
			
			System.out.println("Novo grenal (1-sim 2-nao)");
			grenal = ler.nextInt();
			
			total++;
			
		} while (grenal==1);
		
		if (ccI>ccG) {
			win = "Inter venceu mais"; 
		} else if (ccG>ccI) {
			win = "Gremio venceu mais";
		} else {
			win = "Não houve vencedor";
		}
		
		System.out.println(total+" grenais");
		System.out.println("Inter:"+ccI);
		System.out.println("Gremio:"+ccG);
		System.out.println("Empates:"+ccE);
		System.out.println(win);
		
		ler.close();
	}
}
