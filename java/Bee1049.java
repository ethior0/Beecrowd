import java.util.Scanner;
import java.util.Locale;

public class Bee1049 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		String resposta1, resposta2, resposta3;
		
		resposta1 = ler.next();
		resposta2 = ler.next();
		resposta3 = ler.next();
		
		if (resposta1.equalsIgnoreCase("Vertebrado")) {
			if (resposta2.equalsIgnoreCase("Ave") && resposta3.equalsIgnoreCase("Carnivoro")) {
				System.out.println("aguia");
			} else if (resposta2.equalsIgnoreCase("Ave") && resposta3.equalsIgnoreCase("Onivoro")) {
				System.out.println("pomba");
			}
			if (resposta2.equalsIgnoreCase("Mamifero") && resposta3.equalsIgnoreCase("Onivoro")) {
				System.out.println("homem");
			} else if (resposta2.equalsIgnoreCase("Mamifero") && resposta3.equalsIgnoreCase("Herbivoro")) {
				System.out.println("vaca");
			}
		}
		
		if (resposta1.equalsIgnoreCase("Invertebrado")) {
			if (resposta2.equalsIgnoreCase("Inseto") && resposta3.equalsIgnoreCase("Hematofago")) {
				System.out.println("pulga");
			} else if (resposta2.equalsIgnoreCase("Inseto") && resposta3.equalsIgnoreCase("Herbivoro")) {
				System.out.println("lagarta");
			}
			if (resposta2.equalsIgnoreCase("Anelideo") && resposta3.equalsIgnoreCase("Hematofago")) {
				System.out.println("sanguessuga");
			} else if (resposta2.equalsIgnoreCase("Anelideo") && resposta3.equalsIgnoreCase("Onivoro")) {
				System.out.println("minhoca");
			}
		}
		
		ler.close();
	}
}
