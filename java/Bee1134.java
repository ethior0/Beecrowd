import java.util.Locale;
import java.util.Scanner;

public class Bee1134 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int type, ccA = 0, ccG = 0, ccD = 0;
		
		for (;;){
			type = ler.nextInt();
			switch(type) {
				case 1:
					ccA++;	
					continue;
				case 2:
					ccG++;
					continue;
				case 3:
					ccD++;
					continue;
				case 4:
					break;
				default:
					continue;
			} 	
			
			if (type==4) {
				break;
			}
		}
		
		System.out.println("MUITO OBRIGADO");
		System.out.println("Alcool: "+ccA);
		System.out.println("Gasolina: "+ccG);
		System.out.println("Diesel: "+ccD);
		
		ler.close();
	}
}
