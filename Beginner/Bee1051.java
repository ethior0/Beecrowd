import java.util.Locale;
import java.util.Scanner;

public class Bee1051 {

	public static void main(String[] args) {

		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);

		double salario, imposto = 0, d;

		salario = ler.nextDouble();

		if (salario > 4500) {
			imposto = (1000 * 0.08) + (1500 * 0.18);
			d = salario - 4500;
			imposto += d * 0.28;
		}

		else if (salario > 3000.01 && salario <= 4500) {
			imposto = (1000 * 0.08);
			d = salario - 3000;
			imposto += d * 0.18;
		}

		else if (salario > 2000.01 && salario <= 3000) {
			d = salario - 2000;
			imposto += d * 0.08;
		}

		if (imposto > 0) {
			System.out.printf("R$ %.2f\n", imposto);
		} else {
			System.out.println("Isento");
		}

		ler.close();
	}
}
