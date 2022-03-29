// Fabricio Bertoncello Filho e Felipe Lacerda

import java.util.Scanner;

public class Ex2 {

    public static void fibonacci(int x) {

        int i;

        if (x < 0) {
            System.out.println("Erro! Digite um numero positivo");
        }
        else if (x == 0) {
            System.out.println("0");
        }
        else if (x == 1) {
            System.out.println("0, 1");
        }
        else {
            int n0 = 0, n1 = 1, n2;
            System.out.print("0, 1, ");
            for (i = 1; i < x; i++) {
                n2 = n0 + n1;
                if (i != x-1) {
                    System.out.print(n2 + ", ");
                }
                else {
                    System.out.println(n2);
                }
                n0 = n1;
                n1 = n2;
            }
        }

    }

    public static void main(String args[]) {

        Scanner input = new Scanner(System.in);

        System.out.print("Digite o indice da sequencia de Fibonacci desejado: ");
        int x = input.nextInt();

        input.close();

        fibonacci(x);

    }

}