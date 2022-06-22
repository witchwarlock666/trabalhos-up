import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Scanner;

public class Person {
    private int id;
    private String nm;
    private String rg;
    private Date doB;
    private HashMap<String, String> email = new HashMap<String, String>();
    private HashMap<String, String> phNo = new HashMap<String, String>();;
    private HashMap<String, Address> addr = new HashMap<String, Address>();;

    public Person() {
    }

    public Person(String nm, String rg, Date doB, HashMap email, HashMap phNo, HashMap addr) {
        this.nm = nm;
        this.rg = rg;
        this.doB = doB;
        this.email = email;
        this.phNo = phNo;
        this.addr = addr;
    }

    // #region methods
    public void setPerson(int id) {
        String email1 = "";
        String email2 = "";
        String res = "";
        String com = "";
        String cel = "";
        Address resA = new Address();
        Address comA = new Address();

        Boolean cont = true;
        Scanner input = new Scanner(System.in);

        while (cont) {
            try {
                this.id = id;

                System.out.print("Nome: ");
                this.nm = input.nextLine();

                System.out.print("RG: ");
                this.rg = input.nextLine();

                System.out.print("Data de Nascimento: ");
                this.doB = new SimpleDateFormat("dd/MM/yyyy").parse(input.nextLine());

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

                resA.setAddr();
                comA.setAddr();
                this.email.put("Email Principal", email1);
                this.email.put("Email Secundario", email2);

                this.phNo.put("Telefone Residencial", res);
                this.phNo.put("Telefone Comercial", com);
                this.phNo.put("Telefone Celular", cel);

                this.addr.put("Endereco Residencial", resA);
                this.addr.put("Endereco Comercial", comA);

                cont = false;

            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
    // #endregion

    // #region getters
    public String getNm() {
        return nm;
    }

    public String getRg() {
        return rg;
    }

    public Date getDoB() {
        return doB;
    }

    public HashMap<String, String> getEmail() {
        return email;
    }

    public HashMap<String, String> getPhNo() {
        return phNo;
    }

    public HashMap<String, Address> getAddr() {
        return addr;
    }
    // #endregion

    // #region setters
    public void setId(int id) {
        this.id = id;
    }

    public void setNm(String nm) {
        this.nm = nm;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public void setDoB(Date doB) {
        this.doB = doB;
    }

    public void setEmail(HashMap<String, String> email) {
        this.email = email;
    }

    public void setPhNo(HashMap<String, String> phNo) {
        this.phNo = phNo;
    }

    public void setAddr(HashMap<String, Address> addr) {
        this.addr = addr;
    }
    // #endregion

    @Override
    public String toString() {

        String str = "";
        str += "======== Contato ========\n";
        str += "Id: " + id + "\n";
        str += "Nome: " + nm + "\n";
        str += "RG: " + rg + "\n";
        str += "Data de Nascimento: " + new SimpleDateFormat("dd/MM/yyyy").format(doB) + "\n";
        str += "========= Email =========\n";
        for (String mail : email.keySet()) {
            String key = mail.toString();
            String value = email.get(mail).toString();
            str += key + ": " + value + "\n";
        }
        str += "======== Telefone ========\n";
        for (String ph : phNo.keySet()) {
            String key = ph.toString();
            String value = phNo.get(ph).toString();
            str += key + ": " + value + "\n";
        }
        str += "======== Endereço ========\n";
        for (String add : addr.keySet()) {
            String key = add.toString();
            String value = addr.get(add).toString();
            str += key + ": " + value + "\n";
        }
        // str += "Email Principal: " + email.get("Email Principal") + "\n";
        // str += "Email Secundario: " + email.get("Email Secundario") + "\n";
        // str += "Telefone Residencial: " + email.get("Telefone Residencial") + "\n";
        // str += "Telefone Comercial: " + email.get("Telefone Comercial") + "\n";
        // str += "Telefone Celular: " + email.get("Telefone Celular") + "\n";
        // str += "=== Endereco Residencial ===\n" + email.get("Endereco
        // Residencial").toString() + "\n";
        // str += "==== Endereco Comercial ====\n" + email.get("Endereco
        // Comercial").toString();

        return str;
    }

}
