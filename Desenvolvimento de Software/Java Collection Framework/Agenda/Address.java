import java.util.Scanner;

public class Address {
    private String logradouro;
    private int num;
    private String comp;
    private String district;
    private String cep;
    private String city;

    public Address() {
    }

    public Address(String logradouro, int num, String comp, String district, String cep, String city) {
        this.logradouro = logradouro;
        this.num = num;
        this.comp = comp;
        this.district = district;
        this.cep = cep;
        this.city = city;
    }

    // #region methods

    public void flush_in(Scanner scanner) {
        if (scanner.hasNextLine()) {
            scanner.nextLine();
        }
    }

    public void setAddr() {
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
                this.logradouro = input.nextLine();

                System.out.print("Numero: ");
                this.num = input.nextInt();

                flush_in(input);

                System.out.print("Complemento: ");
                this.comp = input.nextLine();

                System.out.print("Bairro: ");
                this.district = input.nextLine();

                System.out.print("CEP: ");
                this.cep = input.nextLine();

                System.out.print("Cidade: ");
                this.city = input.nextLine();

                cont = false;

            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
    // #endregion

    // #region getters
    public String getLogradouro() {
        return logradouro;
    }

    public int getNum() {
        return num;
    }

    public String getComp() {
        return comp;
    }

    public String getDistrict() {
        return district;
    }

    public String getCep() {
        return cep;
    }

    public String getCity() {
        return city;
    }
    // #endregion

    // #region setters
    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public void setComp(String comp) {
        this.comp = comp;
    }

    public void setDistrict(String district) {
        this.district = district;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }

    public void setCity(String city) {
        this.city = city;
    }
    // #endregion

    @Override
    public String toString() {

        String str = logradouro + ". " + comp + " " + num + ", " + district + ", " + city + ", " + cep;

        return str;
    }

}
