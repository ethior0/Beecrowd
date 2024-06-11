import java.util.Scanner;

public class Main {
	
    public static void main(String[] args) {
    	
        Scanner ler = new Scanner(System.in);
        
        int cc = 1;

        while (true) {
            int N = ler.nextInt();
            if (N == 0) break;

            int[] array = new int[201];
            StringBuilder res = new StringBuilder();
            int maiorIndice = 0, totalX = 0, totalY = 0;

            for (int i = 0; i < N; i++) {
                int X = ler.nextInt();
                int Y = ler.nextInt();
                totalX += X;
                totalY += Y;
                
                int indice = Y / X;
                array[indice] += X;
                if (indice > maiorIndice) {
                    maiorIndice = indice;
                }
            }

            for (int i = 0; i <= maiorIndice; i++) {
                if (array[i] != 0) {
                    res.append(array[i]).append("-").append(i).append(" ");
                }
            }

            double consumoM = (double) totalY / totalX * 100;
            consumoM = Math.floor(consumoM) / 100.0;

            System.out.println("Cidade# " + cc + ":");
            System.out.println(res.toString().trim());
            System.out.printf("Consumo medio: %.2f m3.\n\n", consumoM);
            cc++;
        }
        
        ler.close();
    }
}
