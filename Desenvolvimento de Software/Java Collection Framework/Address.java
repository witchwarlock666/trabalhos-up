public class Address {
    private String logradouro;
    private int num;
    private String comp;
    private String district;
    private String cep;
    private String city;

    public Address(){}

    public Address(String logradouro, int num, String comp, String district, String cep, String city) {
        this.logradouro = logradouro;
        this.num = num;
        this.comp = comp;
        this.district = district;
        this.cep = cep;
        this.city = city;
    }

//#region methods

//#endregion

//#region getters
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
//#endregion

//#region setters
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
//#endregion

}
