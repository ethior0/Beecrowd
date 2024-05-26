import java.util.Locale;

public class Bee1098_3 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		
		double i = 0.2, j = 1.2;
		
		System.out.println("I=0 J=1");
		System.out.println("I=0 J=2");
		System.out.println("I=0 J=3");
		
		for (int d = 0; d<4; d++) {
			System.out.printf("I=%.1f J=%.1f\n", i, j); //quase me frustrei fazendo esse
			System.out.printf("I=%.1f J=%.1f\n", i, j+1); // pq o beecrowd reconheceu o espaço no " \n" 
			System.out.printf("I=%.1f J=%.1f\n", i, j+2); // como erro de apresentacao ;-;
			j += 0.2;
			i += 0.2;
		}
		
		i = 1.2;
		j = 2.2;
		
		System.out.println("I=1 J=2");
		System.out.println("I=1 J=3");
		System.out.println("I=1 J=4");
		
		for (int d = 0; d<4; d++) {
			System.out.printf("I=%.1f J=%.1f\n", i, j);
			System.out.printf("I=%.1f J=%.1f\n", i, j+1);
			System.out.printf("I=%.1f J=%.1f\n", i, j+2);
			j += 0.2;
			i += 0.2;
		}
		
		System.out.println("I=2 J=3");
		System.out.println("I=2 J=4");
		System.out.println("I=2 J=5");
		
	}
}
