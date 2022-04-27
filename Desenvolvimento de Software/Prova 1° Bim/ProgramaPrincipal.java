//Fabricio Bertoncello Filho e Felipe Lacerda

import java.util.Scanner;

public class ProgramaPrincipal {
    public static void main(String[] args) {
        Pessoa[] vet = new Pessoa[6];
        vet[0] = new Pessoa("Felipe", 57, 'M', 90, 100, 80, 30, 70);
        vet[1] = new Pessoa("Maria", 45, 'F', 50, 70, 100, 50, 90);
        vet[2] = new Pessoa("Cristina", 30, 'F', 50, 20, 30, 70, 30);
        vet[3] = new Pessoa("Leonardo", 32, 'M', 80, 10, 60, 80, 50);
        vet[4] = new Pessoa("Joao", 27, 'M', 100, 30, 50, 100, 10);
        vet[5] = new Pessoa("Jessica", 45, 'F', 85, 60, 70, 50, 60);

        Boolean x = true;

        while (x) {
            Scanner input = new Scanner(System.in);

            System.out.print("\nDigite seu nome: ");
            String nome = input.nextLine();
            int idade = 0, gostaViajar = 0, gostaCozinhar = 0, gostaCinema = 0, gostaBalada = 0, gostaFicarEmCasa = 0;
            char genero = 'X';

            while (x) {
                System.out.print("Digite sua idade: ");
                idade = input.nextInt();
                if (idade >= 18)
                    x = false;
            }
            x = true;

            while (x) {
                System.out.print("Digite seu genero: ");
                genero = Character.toUpperCase(input.next().charAt(0));
                if (genero == 'F' || genero == 'M')
                    x = false;
            }
            x = true;

            while (x) {
                System.out.print("Gosta de viajar: ");
                gostaViajar = input.nextInt();
                if (gostaViajar >= 0 && gostaViajar <= 100)
                    x = false;
            }
            x = true;

            while (x) {
                System.out.print("Gosta de cozinhar: ");
                gostaCozinhar = input.nextInt();
                if (gostaCozinhar >= 0 && gostaCozinhar <= 100)
                    x = false;
            }
            x = true;

            while (x) {
                System.out.print("Gosta de cinema: ");
                gostaCinema = input.nextInt();
                if (gostaCinema >= 0 && gostaCinema <= 100)
                    x = false;
            }
            x = true;

            while (x) {
                System.out.print("Gosta de balada: ");
                gostaBalada = input.nextInt();
                if (gostaBalada >= 0 && gostaBalada <= 100)
                    x = false;
            }
            x = true;

            while (x) {
                System.out.print("Gosta de ficar em casa: ");
                gostaFicarEmCasa = input.nextInt();
                if (gostaFicarEmCasa >= 0 && gostaFicarEmCasa <= 100)
                    x = false;
            }
            x = true;

            Pessoa p = new Pessoa(nome, idade, genero, gostaViajar, gostaCozinhar, gostaCinema, gostaBalada,
                    gostaFicarEmCasa);

            double[] resultado = new double[6];

            for (int i = 0; i < 6; i++) {
                if (vet[i].getGenero() != genero) {
                    resultado[i] = p.calcularCompatibilidade(vet[i]);
                } else {
                    resultado[i] = 101;
                }
            }

            int maisCompativel = 0;

            double menor = 101;

            for (int i = 0; i < 6; i++) {
                if (resultado[i] < menor) {
                    maisCompativel = i;
                    menor = resultado[i];
                }
            }

            Pessoa compativel = vet[maisCompativel];

            System.out.printf("\nA pessoa mais compatível com %s é %s.\n", p.getNome(), compativel.getNome());

            System.out.println("\nDados da pessoa informada:\n");

            System.out.println(p.toString());

            System.out.println("\nDados da pessoa mais compativel:\n");

            System.out.println(compativel.toString());

            char sair = 'X';

            System.out.print("\nDeseja continuar: ");
            sair = Character.toUpperCase(input.next().charAt(0));
            if (sair == 'S')
                x = false;

            input.close();
        }
    }
}
