import java.util.Locale;
import java.util.Scanner;

public class Bee1144 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		
		int num = 1, num2, num3;
		int n = ler.nextInt();
		
		for (int i = 0; i <n; i++) {
			
		int f = 0;
		
		while (f<2) {
			System.out.print(num+" ");
			num2 = num*num;
			System.out.print((num2+f)+" ");
			num3 = num2*num;
			System.out.println(num3+f);
			f++;
			}
		
			num++;
		}
		
		
		ler.close();
	}
}
