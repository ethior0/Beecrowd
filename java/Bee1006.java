import java.util.Scanner;

public class Bee1006 {
	public static void main (String[] args) 
	{
		
		Scanner ler = new Scanner (System.in);
		
		double A, B, C, MEDIA;
		
		A = ler.nextDouble();
		B = ler.nextDouble();
		C = ler.nextDouble();
		
		MEDIA = ((A*2)+(B*3)+(C*5))/10;
		
		System.out.format("MEDIA = %.1f\n", MEDIA);
		ler.close();
		
	}
}
