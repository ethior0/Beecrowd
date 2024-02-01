import java.util.Scanner;

public class Bee1009 {
	public static void main (String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		String name;
		double salary, sale, TOTAL;
		
		name = ler.next();
		salary = ler.nextDouble();
		sale = ler.nextDouble();
		
		TOTAL = salary+(sale*0.15);
		
		System.out.format("TOTAL = R$ %.2f\n", TOTAL);
		ler.close();
		
	}
}