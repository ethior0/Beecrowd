import java.util.Scanner;

public class Bee1234 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		while (ler.hasNext()) {
			
			String newSen = "", sen = ler.nextLine();
			sen = sen.toUpperCase();
			int aux = 0;
			
			for (int i = 0; i < sen.length(); i++) {
				if (sen.charAt(i) > 64 && sen.charAt(i) < 91) {
					String letter = sen.charAt(i) + "";
					newSen += aux % 2 == 0 ? letter.toUpperCase() : letter.toLowerCase();
					aux++;
				} else {
					newSen += sen.charAt(i);
				}
			}
			
			System.out.println(newSen);
		}
		
		ler.close();
	}
}
