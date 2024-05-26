import java.util.Locale;

public class Bee1098 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		
		double i = 0, j = 1, newJ = 1;
		
		while (i<=2) {
			j = newJ;
			do {
				System.out.printf("I=%.1f J=%.1f \n", i, j);
				j++;
			} while(j<4);
			i += 0.2;
			newJ = 1.2;
		}
	}
}
