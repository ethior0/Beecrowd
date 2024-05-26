import java.util.Scanner;

public class Bee2473 {

	public static void main(String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int pontos = 0;
	
		String a = ler.nextLine();
		String[] aArr = a.split(" ");
		String r = ler.nextLine();
		String[] rArr = r.split(" ");
		
		for (int i = 0; i < 6; i++) {
			for (int j = 0; j < 6; j++) {
				if ( aArr[i].equals(rArr[j]) ) pontos++;
			}
		}
		
		if (pontos < 3) {
			System.out.println("azar");
		} else {
			switch(pontos) {
			case 3:
				System.out.println("terno");
				break;
			case 4:
				System.out.println("quadra");
				break;
			case 5:
				System.out.println("quina");
				break;
			case 6:
				System.out.println("sena");
				break;
			}
		}
		
		ler.close();
	}
}
