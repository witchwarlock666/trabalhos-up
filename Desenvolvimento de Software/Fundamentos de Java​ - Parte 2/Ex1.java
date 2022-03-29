// Fabricio Bertoncello Filho e Felipe Lacerda

import java.util.Scanner;

public class Ex1 {

    public static void main(String args[]) {

        Scanner myObj = new Scanner(System.in);

        int acumulo;

        System.out.print("Olá, digite o número desejado para fatorial: ");

        int x = myObj.nextInt();

        myObj.close();

        int i;

        acumulo = 1;

        if (x > 0) {

            for (i = x; i > 0; i--) {

                acumulo = acumulo * i;

            }

            System.out.print(x + "! = " + acumulo);

        } else if (x == 0) {

            System.out.print(x + "! = " + acumulo);

        } else {
            System.out.print("Impossivel calcular fatorial de numeros negativos.");
        }

    }

}