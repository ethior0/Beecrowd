import java.util.Locale;
import java.util.Scanner;

public class Bee1114 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int senha = 2002;
		
		for (;;) {
			
			int teste = ler.nextInt();
			
			if (teste==senha) {
				System.out.println("Acesso Permitido");
				break;
			} else {
				System.out.println("Senha Invalida");
			}
			
			ler.close();
		}
	}
}
