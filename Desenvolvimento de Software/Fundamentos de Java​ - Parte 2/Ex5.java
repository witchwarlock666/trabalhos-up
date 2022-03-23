import java.util.Random;
import java.util.Scanner;

public class Ex5 {
    public static void main(String[] args) {
        Random random = new Random();
        int i, n, j, acertos;
        int[] loto = new int[6];
        int[] user = new int[6];
        boolean teste;

        for (i = 0; i < 6; i++) {
            teste = false;
            n = 1 + random.nextInt(60);
            for (j = 0; j < loto.length; j++) {
                if (n == loto[j]) {
                    teste = true;
                }
            }
            
            if (!teste) {
                loto[i] = n;
            } else {
                i--;
            }
        }
        // for (i = 0; i < 6; i++) {
        //     System.out.println(loto[i]);
        // }
        Scanner input = new Scanner(System.in);
            System.out.println("Digite seus numeros:");
        for (i = 0; i < 6; i++) {
            teste = false;
            n = input.nextInt();
            for (j = 0; j < user.length; j++) {
                if (n == user[j]) {
                    teste = true;
                }
            }
            
            if (!teste) {
                user[i] = n;
            } else {
                i--;
            }
        }
        // for (i = 0; i < 6; i++) {
        //     System.out.println(user[i]);
        // }

        System.out.print("Numeros sorteados: ");
        for (i = 0; i < 5; i++) {
            System.out.print(loto[i] + ", ");
        }
        System.out.println(loto[5]);

        acertos = 0;

        for (i = 0; i < 6; i++) {
            for (j = 0; j < 6; j++) {
                if (user[i] == loto[j]) {
                    acertos++;
                }
            }
        }
        if (acertos < 4) {
            System.out.print("Parabéns! Você não ganhou nada!" );
        }
        else if (acertos == 4) {
            System.out.print("Parabéns! Você ganhou R$50.000,00!" );
        }
        else if (acertos == 5) {
            System.out.print("Parabéns! Você ganhou R$250.000,00!" );
        }
        else if (acertos == 6) {
            System.out.print("Parabéns! Você ganhou R$1.000.000,00!" );
        }
    }
}