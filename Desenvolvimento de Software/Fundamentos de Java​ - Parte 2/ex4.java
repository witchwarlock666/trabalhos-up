// Fabricio Bertoncello Filho e Felipe Lacerda

import java.util.Scanner;

public class Ex4 {

    public static void main(String args[]) {
        Scanner catador = new Scanner(System.in);

        int x;
        int i, j;
        int y, yp;
        y = 0;
        yp = 0;
        int[] a = new int[100];

        System.out.println("Digite o valor de x: ");
        x = catador.nextInt();

        System.out.println("Digite o vlor de n: ");
        j = catador.nextInt();

        if (j <= 0 || x <= 0) {
            System.out.println("Valor invalido");
        }

        else {
            for (i = 0; i < j; i++) {
                System.out.printf("Digite o A de posiçao %d: ", i + 1);
                a[i] = catador.nextInt();

            }

            i = j;
            while (i > 0) {
                y += a[i] * Math.pow(x, i--);
            }
            System.out.printf("y = %d\n", y);

            i = j;
            while (i > 0) {
                yp += i * a[i] * Math.pow(x, --i);
            }
            System.out.printf("y'= %d", yp);
        }
        catador.close();
    }
}
