
public class Bee1097 {

	public static void main(String[] args) {
		
		int i = 1, j = 7;
		
		while (i<=9) {
			int cc = 0;
			
			do {
				System.out.println("I="+i+" J="+j);
				j--;
				cc++;
			} while (cc<3);
			
			i += 2;
			j += 5;
		}
	}
}
