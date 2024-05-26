package bee1534;

import java.util.Arrays;
import java.util.Scanner;

public class Bee1534 {

    public static void main(String[] args) {

        Scanner ler = new Scanner(System.in);

        while (ler.hasNext()) {

            int num = ler.nextInt();
            int matriz[] = new int[num];
            int aux = 0, aux2 = num - 1;

            for (int i = 0; i < num; i++) {

                Arrays.fill(matriz, 3);
                matriz[aux] = 1;
                matriz[aux2] = 2;
                aux++;
                aux2--;

                for (int j = 0; j < num; j++) {
                    System.out.print(matriz[j]);
                }
                System.out.println("");
            }
        }
        
        ler.close();
    }
}
