package bee1534;

import java.util.Scanner;

public class Bee1534_2 {
    
    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);
        int n = leitor.nextInt();
        int x[][] = new int[n][n];
        int i, j;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                if (j == n - i - 1) {
                    x[i][j] = 2;
                } else if (i == j) {
                    x[i][j] = 1;
                } else {
                    x[i][j] = 3;
                }
                System.out.print(x[i][j]);
            }
            System.out.println();
        }
    }
}
