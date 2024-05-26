import java.util.Locale;

public class Bee1098_2 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		
		double i = 0.2, j = 1.2, newJ = 1.2;
		
		System.out.println("I=0 J=1");
		System.out.println("I=0 J=2");
		System.out.println("I=0 J=3");
		
		
		while (i<=2) {
			j = newJ;
			do {
				System.out.printf("I=%.1f J=%.1f \n", i, j);
				j++;
			} while(j<=4);
			i += 0.2;
			newJ += 0.2;
		}
	}
}
