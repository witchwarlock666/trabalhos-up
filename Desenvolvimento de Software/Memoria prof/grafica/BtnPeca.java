//Fabricio Bertoncello Filho e Felipe Lacerda

package grafica;

import javax.swing.JToggleButton;

public class BtnPeca extends JToggleButton{
    private int num;
    public int i, j;
    public BtnPeca(int num, int i, int j) {
        this.num = num;
        this.i = i;
        this.j = j;
        setSize(15, 15);
    }    

    public void mostrar() {
        setSelected(true);
        setText(Integer.toString(num));
    }

    public void ocultar(){
        setSelected(false);
        setText("");
    }

    public int getNumero() {
        return num;
    }
}
