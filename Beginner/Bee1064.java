import java.util.Scanner;
import java.util.Locale;

public class Bee1064 {
    
    public static void main(String[] args) {
        
        Locale.setDefault(Locale.US);
        Scanner ler = new Scanner(System.in);
        
        int cont = 0;
        double media = 0;
        double x;
        
        for (int i = 0; i < 6; i++) {
        	x = ler.nextDouble();
        	if (x>0) {
        		cont++;
        		media += x;
        	}
        }
        
        media = media / cont; 
        System.out.println(cont + " valores positivos");
        System.out.printf(String.format("%.1f \n", media));
               
        ler.close();
    }
}