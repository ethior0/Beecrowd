import java.util.Scanner;

public class Bee1024ex2 {

	// funciona, mas é time limit exceeded :I
	public static void main(String[] args) {

		Scanner ler = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();

		int N = ler.nextInt();
		ler.nextLine();

		for (int i = 0; i < N; i++) {
            String texto = ler.nextLine();
            String novoTexto = substituirLetras(texto);
            sb.append(novoTexto);

            for (int j = 0; j < (float) novoTexto.length() / 2; j++) {
            	sb.replace(j, j, (char) sb.charAt(j) - 1 + "");
            }
            
            System.out.println(sb.reverse().toString());
            sb.delete(0, novoTexto.length());
		}

		ler.close();
	}

	private static String substituirLetras(String texto) {
		
		StringBuilder novoTexto = new StringBuilder();

		for (int j = 0; j < texto.length(); j++) {
			char caractere = texto.charAt(j);

			if (Character.isLetter(caractere)) {
				char base = Character.isLowerCase(caractere) ? 'a' : 'A';
				char novaLetra = (char) ((caractere - base + 3) % 26 + base);
				novoTexto.append(novaLetra);
			} else {
				novoTexto.append(caractere);
			}
		}

		return novoTexto.toString();
	}
}
