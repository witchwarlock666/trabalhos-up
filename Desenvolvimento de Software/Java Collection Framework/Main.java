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
        List contatos = new ArrayList<Person>();
        Scanner input = new Scanner(System.in);
        int op;

        do {
            clear();
            System.out.println(
                    "===== Menu =====\n\n[ 1 ] Criar Contato\n[ 2 ] Listar Contatos\n[ 3 ] Editar Contato\n[ 4 ] Deletar Contato\n[ 0 ] Sair");
            op = input.nextInt();

            switch (op) {
                case 1:
                    contatos.add(create());
                    id++;
                    break;
                case 2:
                    list(contatos);
                    break;
                case 3:
                    // edit();
                    break;
                case 4:
                    // delete();
                    break;
            }
        } while (op != 0);
    }

    private static Person create() {
        String rg = "";
        String nm = "";
        Date doB = new Date();
        String email1 = "";
        String email2 = "";
        String res = "";
        String com = "";
        String cel = "";
        Address resA = new Address();
        Address comA = new Address();
        HashMap<String, String> email = new HashMap<String, String>();
        HashMap<String, String> phNo = new HashMap<String, String>();
        HashMap<String, Address> addr = new HashMap<String, Address>();

        Boolean cont = true;
        Scanner input = new Scanner(System.in);

        while (cont) {
            try {
                System.out.print("Nome: ");
                nm = input.nextLine();

                System.out.print("RG: ");
                rg = input.nextLine();

                System.out.print("Data de Nascimento: ");
                doB = new SimpleDateFormat("dd/MM/yyyy").parse(input.nextLine());

                System.out.print("Email Principal: ");
                email1 = input.nextLine();

                System.out.print("Email Secundario: ");
                email2 = input.nextLine();

                System.out.print("Telefone Residencial: ");
                res = input.nextLine();

                System.out.print("Telefone Comercial: ");
                com = input.nextLine();

                System.out.print("Telefone Celular: ");
                cel = input.nextLine();

                resA = newAddr();
                comA = newAddr();
                email.put("Email Principal", email1);
                email.put("Email Secundario", email2);

                phNo.put("Telefone Residencial", res);
                phNo.put("Telefone Comercial", com);
                phNo.put("Telefone Celular", cel);

                addr.put("Endereco Residencial", resA);
                addr.put("Endereco Comercial", comA);

                cont = false;

            } catch (Exception e) {
            }
        }

        return new Person(id, nm, rg, doB, email, phNo, addr);
    }

    private static Address newAddr() {
        String logradouro = "";
        int num = 0;
        String comp = "";
        String district = "";
        String cep = "";
        String city = "";

        Boolean cont = true;
        Scanner input = new Scanner(System.in);

        while (cont) {
            try {
                System.out.print("Logradouro: ");
                logradouro = input.nextLine();

                System.out.print("Numero: ");
                num = input.nextInt();

                input.nextLine();

                System.out.print("Complemento: ");
                comp = input.nextLine();

                System.out.print("Bairro: ");
                district = input.nextLine();

                System.out.print("CEP: ");
                cep = input.nextLine();

                System.out.print("Cidade: ");
                city = input.nextLine();

                cont = false;

            } catch (Exception e) {
            }
        }
        return new Address(logradouro, num, comp, district, cep, city);
    }

    private static void list(List person) {
        Scanner cont = new Scanner(System.in);
        person.forEach(item -> System.out.println(item));
        cont.nextLine();
    }
}
