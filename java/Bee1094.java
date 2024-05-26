import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;

public class Bee1094 {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner ler = new Scanner(System.in);
		DecimalFormat dec = new DecimalFormat("#0.00");
		
		int total = 0, coelho = 0, rato = 0, sapo = 0;
		
		int count = ler.nextInt();
		
		for (int i = 0; i<count; i++) {
			
			int quantidade = ler.nextInt();
			
			String tipo = ler.next();
			
			total += quantidade; 
			
			if (tipo.equalsIgnoreCase("C")) {
				coelho += quantidade;
			} 
			if (tipo.equalsIgnoreCase("R")) {
				rato += quantidade;
			}
			if (tipo.equalsIgnoreCase("S")) {
				sapo += quantidade;
			}
		}
		
		double percentualC = (double) coelho/total*100;
		double percentualR = (double) rato/total*100;
		double percentualS = (double) sapo/total*100;
		
		System.out.println("Total: " + total + " cobaias");
		System.out.println("Total de coelhos: " + coelho);
		System.out.println("Total de ratos: " + rato);
		System.out.println("Total de sapos: " + sapo);
		
		System.out.println("Percentual de coelhos: "+dec.format(percentualC)+ " %");
		System.out.println("Percentual de ratos: "+dec.format(percentualR)+ " %");
		System.out.println("Percentual de sapos: "+dec.format(percentualS)+" %");
		
//		System.out.printf("Percentual de coelhos: %.2f %%\n", percentualC);
//		System.out.printf("Percentual de ratos: %.2f %%\n", percentualR);
//		System.out.printf("Percentual de sapos: %.2f %%\n", percentualS);
		
		ler.close();
	}
	
}
