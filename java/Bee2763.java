import java.util.Scanner;

public class Bee2763 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		String cpf = ler.next();
		cpf = cpf.replace(".", "").replace("-", "");
		
		System.out.format( "%c%c%c\n", cpf.charAt(0), cpf.charAt(1), cpf.charAt(2) );
		System.out.format( "%c%c%c\n", cpf.charAt(3), cpf.charAt(4), cpf.charAt(5) );
		System.out.format( "%c%c%c\n", cpf.charAt(6), cpf.charAt(7), cpf.charAt(8) );
		System.out.format( "%c%c", cpf.charAt(9), cpf.charAt(10) );
				
		ler.close();
	}
}
