import java.util.Scanner;
import java.util.Locale;

/* gambiarra (?)
 * top
 * q nao funcionou
 * ...
 */


public class Bee1040 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		float exam;
		
		double n1 = ler.nextDouble();
		double n2 = ler.nextDouble();
		double n3 = ler.nextDouble();
		double n4 = ler.nextDouble();
		
		double average = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10;
		
		System.out.printf("Media: %.1f%n", average);
		
		if (average>=7) { 
			System.out.println("Aluno aprovado.");
		}
		
		if (average<5) { 
			System.out.println("Aluno reprovado.");
		}
		
		exam = ler.nextFloat();
		average = (average+exam)/2;
		
		if (average>=5 && average<=6.9) { 
			System.out.println("Aluno em exame.");
		
			System.out.printf("Nota do exame: %.1f%n"+exam);
			
			if (average>=5) {
				System.out.println("Aluno aprovado.");
			}
			if (average<=4.9) {
				System.out.println("Aluno reprovado.");
			}
		}
		
		System.out.printf("Media final: %.1f%n"+average);
		
		ler.close();
	}
}
