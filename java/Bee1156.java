
public class Bee1156 {

	public static void main(String[] args) {
		
		double s = 1;
		double n = 3;
		
		for (double i = 2; n<=39; i*=2) {
			s += n/i;
			n += 2;
		}
		
		System.out.printf("%.2f\n",s);
		
	}
}
