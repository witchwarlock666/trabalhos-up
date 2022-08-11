//Fabricio Bertoncello Filho e João Lucas de Oliveira Vieira

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Main {

    static int id = 1;

    public static void clear() {
        try {
            if (System.getProperty("os.name").contains("Windows"))
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            else
                Runtime.getRuntime().exec("clear");
        } catch (Exception e) {
        }
    }

    public static void main(String args[]) {
        ArrayList<Person> contatos = new ArrayList<Person>();
        Scanner input = new Scanner(System.in);
        int op;

        do {
            clear();
            System.out.println(
                    "===== Menu =====\n\n[ 1 ] Criar Contato\n[ 2 ] Listar Contatos\n[ 3 ] Editar Contato\n[ 4 ] Deletar Contato\n[ 0 ] Sair");
            op = input.nextInt();

            switch (op) {
                case 1:
                    clear();
                    contatos.add(create());
                    id++;
                    break;
                case 2:
                    list(contatos);
                    break;
                case 3:
                    edit(contatos);
                    break;
                case 4:
                    delete(contatos);
                    break;
            }
        } while (op != 0);
    }

    public static Person create() {
        Person person = new Person();
        person.setPerson(id);
        return person;
    }

    public static void list(ArrayList list) {
        ArrayList contatos = sort(list);
        Scanner in = new Scanner(System.in);
        try {
            for (int i = 0; i < contatos.size(); i++) {
                clear();
                String s = contatos.get(i).toString();
                System.out.println(s);
                in.nextLine();
            }
        } catch (Exception e) {
            System.out.println(e);
            in.nextLine();
        }
    }

    public static void edit(ArrayList contatos) {
        Scanner in = new Scanner(System.in);
        try {
            System.out.print("Digite o id do contato: ");
            int id = in.nextInt();
            Person p = new Person();
            p.setPerson(id);
            contatos.set(id-1, p);
        } catch (Exception e) {
            System.out.println(e);
            in.nextLine();
        }
    }

    public static void delete(ArrayList<Person> contatos) {
        Scanner in = new Scanner(System.in);
        try {
            System.out.print("Digite o id do contato: ");
            int i = in.nextInt();
            contatos.remove(i-1);
            i++;
            for (Person p : contatos) {
                p.setId(i-1);
                i++;
            }
            id--;
        } catch (Exception e) {
            System.out.println(e);
            in.nextLine();
        }
    }

    public static ArrayList<Person> sort(ArrayList<Person> contatos) {
        Person temp;
        for (int i = 0; i < contatos.size(); i++) {
            for (int j = i + 1; j < contatos.size(); j++) {
                if (contatos.get(i).getNm().compareTo(contatos.get(j).getNm()) > 0) {
                    // swapping
                    temp = contatos.get(i);
                    contatos.set(i, contatos.get(j));
                    contatos.set(j, temp);
                }
            }
        }

        return contatos;
    }
}
