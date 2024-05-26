import java.util.Scanner;

public class Bee1120 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int D = ler.nextInt();
		String L = ler.next();
		sb.append(L.replaceAll(D + "", ""));
		
		while (D != 0) {
			for (int i = 0; i < sb.length(); i++) {
				if (sb.charAt(i) == '0' && i < sb.length() - 1) {
					sb.setCharAt(i, 't');
				} else {
					break;
				}
			}
			System.out.println(sb.length() == 0 ? 0 : sb.toString().replaceAll("t", ""));
			sb.delete(0, sb.length());
			
			D = ler.nextInt();
			L = ler.next();
			
			sb.append(L.replaceAll(D + "", ""));
		}
		
		ler.close();
	}
}
