import java.util.Scanner;
public class Bee1002 {
	public static void main (String[] args) {
		Scanner ler = new Scanner(System.in);
		
		double R, A;
		
		R = ler.nextDouble();
		
		A = 3.14159*(R*R);
		
		//DETALHE: PARA LIMITAR AS CASAS DECIMAIS -> %.4f (QUATRO DIGITOS DEPOIS DA VÍRGULA)
		// E NAO SE ESQUEÇA DA "," ANTES DA VARIAVEL
		
		System.out.format("A=%.4f\n", A);
		ler.close();
	}
}
