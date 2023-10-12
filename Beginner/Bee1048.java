import java.util.Locale;
import java.util.Scanner;

public class Bee1048 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double Newsalary;
		
		double salary = ler.nextDouble();
		
		if (salary<=400) {
			Newsalary = salary*1.15;
			System.out.printf("Novo salario: %.2f\n", Newsalary);
			System.out.printf("Reajuste ganho: %.2f\n", salary*0.15);
			System.out.println("Em percentual: 15 %");
		} else if (salary<=800) {
			Newsalary = salary*1.12;
			System.out.printf("Novo salario: %.2f\n", Newsalary);
			System.out.printf("Reajuste ganho: %.2f\n", salary*0.12);
			System.out.println("Em percentual: 12 %");
		} else if (salary<=1200) {
			Newsalary = salary*1.10;
			System.out.printf("Novo salario: %.2f\n", Newsalary);
			System.out.printf("Reajuste ganho: %.2f\n", salary*0.10);
			System.out.println("Em percentual: 10 %");
		} else if (salary<=2000) {
			Newsalary = salary*1.07;
			System.out.printf("Novo salario: %.2f\n", Newsalary);
			System.out.printf("Reajuste ganho: %.2f\n", salary*0.07);
			System.out.println("Em percentual: 7 %");
		} else {
			Newsalary = salary*1.04;
			System.out.printf("Novo salario: %.2f\n", Newsalary);
			System.out.printf("Reajuste ganho: %.2f\n", salary*0.04);
			System.out.println("Em percentual: 4 %");
		}
		
		
		ler.close();
	}
}
