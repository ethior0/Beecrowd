import java.util.Scanner;

public class Bee1026 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		while(ler.hasNext()) {
			
			String linha = ler.nextLine();
			String numeros[] = linha.split(" ");
			
			String num1 = Long.toBinaryString(Long.parseLong( numeros[0]) );
			String num2 = Long.toBinaryString(Long.parseLong( numeros[1]) );
			
			while (num1.length() < num2.length() || num2.length() < num1.length()) {
				if (num1.length() < num2.length()) {
					num1 = "0" + num1;
				}
				if (num2.length() < num1.length()) {
					num2 = "0" + num2;
				}
			}
			
			String output = "";
			for (int j = 0; j < num1.length(); j++) {
					
				if (num1.charAt(j) == num2.charAt(j) && num2.charAt(j) == '1') {
					output += "0";
				}
				if (num1.charAt(j) == num2.charAt(j) && num1.charAt(j) == '0') {
					output += "0";
				}
				if (num1.charAt(j) != num2.charAt(j)) {
					output += "1";
				}
			}

			System.out.println(Long.parseLong(output, 2));
		}
	
		ler.close();
	}
}
