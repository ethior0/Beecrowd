import java.io.IOException;
import java.util.Scanner;

public class Bee1168 {

	public static void main(String[] args) throws IOException {
		
		Scanner ler = new Scanner(System.in);
		int n = ler.nextInt();
		
		for (int i = 0; i < n; i++) {
			String num = ler.next();
			int led = 0;
			
			for (int j = 0; j < num.length(); j++) {
				if (num.charAt(j) == '0') led += 6;
                else if (num.charAt(j) == '1') led += 2;
                else if (num.charAt(j) == '2') led += 5;
                else if (num.charAt(j) == '3') led += 5;
                else if (num.charAt(j) == '4') led += 4;
                else if (num.charAt(j) == '5') led += 5;
                else if (num.charAt(j) == '6') led += 6;
                else if (num.charAt(j) == '7') led += 3;
                else if (num.charAt(j) == '8') led += 7;
                else if (num.charAt(j) == '9') led += 6;
			}
			System.out.println(led + " leds");
		}
		
		ler.close();
	}
}
