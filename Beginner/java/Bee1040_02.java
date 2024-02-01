import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Scanner;

//solução certa

public class Bee1040_02 {
	
	public static void main(String[] args) throws IOException {
		
		Scanner ler = new Scanner(System.in);
		DecimalFormat df = new DecimalFormat("0.0");
		
		double N1 = ler.nextDouble();
		double N2 = ler.nextDouble();
		double N3 = ler.nextDouble();
		double N4 = ler.nextDouble();
		
        double MEDIA = ((N1*2) + (N2*3) + (N3*4) + (N4*1)) / 10;
        
		System.out.println("Media: " + df.format(MEDIA));
		
        if (MEDIA >= 7) {
        	System.out.println("Aluno aprovado.");
        } else if (MEDIA < 7 && MEDIA >= 5) {
        	
        	System.out.println("Aluno em exame.");
        	double NExame = ler.nextDouble();
        	
			System.out.println("Nota do exame: " + df.format(NExame));
        	MEDIA = (MEDIA + NExame) / 2;
        	
        	if (MEDIA >= 5) {
            	System.out.println("Aluno aprovado.");
        	} else {
            	System.out.println("Aluno reprovado.");
        	}
			System.out.println("Media final: " + df.format(MEDIA));
        } else {
        	System.out.println("Aluno reprovado.");
        }
  
        
        ler.close();
	}
	
}