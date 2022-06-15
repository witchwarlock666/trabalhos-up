import java.util.Date;
import java.util.HashMap;

public class Person {
    private int id;
    private String nm;
    private String rg;
    private Date doB;
    private HashMap<String, String> email;
    private HashMap<String, String> phNo;
    private HashMap<String, Address> addr;

    public Person(){}

    public Person(int id, String nm, String rg, Date doB, HashMap email, HashMap phNo, HashMap addr) {
        this.id = id;
        this.nm = nm;
        this.rg = rg;
        this.doB = doB;
        this.email = email;
        this.phNo = phNo;
        this.addr = addr;
    }

//#region getters
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
//#endregion

////#region setters
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
//#endregion
}
