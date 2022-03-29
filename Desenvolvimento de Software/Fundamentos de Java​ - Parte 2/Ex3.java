// Fabricio Bertoncello Filho e Felipe Lacerda

import java.util.Random;
import java.util.Scanner;

public class Ex3 {

    public static void main(String args[]) {

        int i;
        Random rand = new Random();
        int n = rand.nextInt(101);

        Scanner input = new Scanner(System.in);

        for (i = 0; i < 10; i++) {
            System.out.print("Digite um numero de 0 a 100: ");
            int x = input.nextInt();

            if (x > n) {
                System.out.println("O numero digitado é maior que o alvo.");
            }
            else if (x < n) {
                System.out.println("O numero digitado é menor que o alvo.");
            }
            else {
                System.out.println("Parabens, voce acertou!");
                break;
            }
        }
        input.close();

    }

}