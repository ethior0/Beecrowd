import java.util.Scanner;

public class Bee1008 {
	public static void main (String[] args) {
		
		Scanner ler = new Scanner(System.in);
		
		int number, workedHour;
		double amountHour, SALARY;
		
		number = ler.nextInt();
		workedHour = ler.nextInt();
		amountHour = ler.nextDouble();
		
		SALARY = amountHour*workedHour;
		
		System.out.println("NUMBER = "+number);
		System.out.format("SALARY = U$ %.2f\n", SALARY);
		ler.close();
		
	}
}
