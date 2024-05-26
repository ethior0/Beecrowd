import java.util.Scanner;

public class Bee1024 {
	
	public static void main (String[] args) {
		
		Scanner ler = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int N = ler.nextInt();
		ler.nextLine();
		
		for (int i = 0; i < N; i++) {
			String text = ler.nextLine();
			String newWord = "";
			
			for (int j = 0; j < text.length(); j++) {
				if (text.charAt(j) > 64 && text.charAt(j) < 91 || text.charAt(j) > 96 && text.charAt(j) < 123) {
					if (j < (float) text.length() / 2 ) {
						newWord += (char) ((int)text.charAt(j) + 2);
					} else {
						newWord += (char) ((int)text.charAt(j) + 3);
					}
				} else {
					if (j < (float) text.length() / 2 ) {
						newWord += (char) ((int)text.charAt(j) - 1);
					} else {
						newWord += text.charAt(j);
					}
				}
			}
			sb.append(newWord);
			System.out.println(sb.reverse().toString());
			sb.delete(0, newWord.length());
		}
		
		ler.close();
	}
}
