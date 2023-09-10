import java.util.Scanner;

public class Bee1005 
{
	public static void main (String[] args) 
	{
		
		Scanner ler = new Scanner(System.in);
		
		double A, B, MEDIA;
		
		A = ler.nextDouble();	
		B = ler.nextDouble();

		MEDIA = ((A*3.5)+(B*7.5))/11;
				
		System.out.format("MEDIA = %.5f\n", MEDIA);
		ler.close();
	}
}

/**
import java.util.Scanner;

public class Average01 
{
	public static void main (String[] args) 
	{
		
		Scanner ler = new Scanner(System.in);
		
		double A, B, MEDIA;
		
		A = ler.nextDouble();
		if (A > 10) {A = 10;}
		if (A < 0) {A = 0;}
		
		B = ler.nextDouble();
		if (B > 10) {B = 10;}
		if (B < 0) {B = 0;}
		
		MEDIA = ((A*3.5)+(B*7.5))/11;
				
		System.out.format("MEDIA = %.5f\n", MEDIA);
		ler.close();
	}
}
*/