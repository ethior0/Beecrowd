import java.util.Scanner;
import java.util.Locale;

public class Bee1021 {
	
	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		double valueI = ler.nextDouble();
		int value = 0;
		
		System.out.println("NOTAS:");
		
		value = (int) valueI / 100;
		System.out.printf("%d nota(s) de R$ 100.00%n", value);
		valueI = valueI % 100.0;
		
		value = (int) valueI / 50;
		System.out.printf("%d nota(s) de R$ 50.00%n", value);
		valueI = valueI % 50.0;
		
		value = (int) valueI / 20;
		System.out.printf("%d nota(s) de R$ 20.00%n", value);
		valueI = valueI % 20.0;

		value = (int) valueI / 10;
		System.out.printf("%d nota(s) de R$ 10.00%n", value);
		valueI = valueI % 10.0;
		
		value = (int) valueI / 5;
		System.out.printf("%d nota(s) de R$ 5.00%n", value);
		valueI = valueI % 5.0;
		
		value = (int) valueI / 2;
		System.out.printf("%d nota(s) de R$ 2.00%n", value);
		valueI = valueI % 2.0;
		
		valueI = valueI * 100.0;
		
		System.out.println("MOEDAS:");
		
		value = (int) valueI / 100;
		System.out.printf("%d moeda(s) de R$ 1.00%n", value);
		valueI = valueI % 100.0;
		
		value = (int) valueI / 50;
		System.out.printf("%d moeda(s) de R$ 0.50%n", value);
		valueI = valueI % 50.0;
		
		value = (int) valueI / 25;
		System.out.printf("%d moeda(s) de R$ 0.25%n", value);
		valueI = valueI % 25.0;
		
		value = (int) valueI / 10;
		System.out.printf("%d moeda(s) de R$ 0.10%n", value);
		valueI = valueI % 10.0;
		
		value = (int) valueI / 5;
		System.out.printf("%d moeda(s) de R$ 0.05%n", value);
		valueI = valueI % 5.0;
		
		value = (int) valueI / 1;
		System.out.printf("%d moeda(s) de R$ 0.01%n", value);
		valueI = valueI % 1.0;
		
		ler.close();
	}
}