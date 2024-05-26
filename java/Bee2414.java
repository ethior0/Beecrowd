import java.util.Scanner;

public class Bee2414 {

	public static void main (String[] args) {
		
		Scanner ler = new Scanner(System.in);

		int cc = 0, maior = 0, cc1 = 0, tamanho;
		
		String numbers[] = ler.nextLine().split(" ");
		tamanho = numbers.length;
		
		if (Integer.parseInt(numbers[tamanho-1]) == 0) {
			while (Integer.parseInt(numbers[cc1]) != 0) {
				if (Integer.parseInt(numbers[cc1]) > maior) {
					maior = Integer.parseInt(numbers[cc1]);
				}
				cc1++;
			}
		} 
		
		System.out.println(maior);
		
		ler.close();
	}
}