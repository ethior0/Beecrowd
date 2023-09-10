import java.util.Scanner;

public class Bee1007 {
    public static void main (String[] args) {
        
        Scanner ler = new Scanner (System.in);
        
        int A, B, C, D, DIFERENCA;
        
        A = ler.nextInt();
        B = ler.nextInt();
        C = ler.nextInt();
        D = ler.nextInt();
        
        DIFERENCA = (A*B)-(C*D);
        
        System.out.println("DIFERENCA = "+DIFERENCA);
        ler.close();
    }
}