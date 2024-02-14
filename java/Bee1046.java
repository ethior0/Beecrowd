import java.util.Scanner;
import java.util.Locale;

public class Bee1046 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int startT, endT, time = 0;
		
		startT = ler.nextInt();
		endT = ler.nextInt();
		
		
		if (startT==endT) {
			time = Math.abs((24 - endT)+ startT);
		} 
		else if (startT<endT) {
			time = Math.abs(startT - endT);
		}
		else if (startT>endT) {
			time = Math.abs((24 - startT)+ endT);
		}
		
		System.out.println("O JOGO DUROU "+time+" HORA(S)");
		
		ler.close();
	}
}
