// Felipe Lacerda E Fabricio Bertoncelo
package grafica;

import javax.swing.JToggleButton;

public class BtnPeca extends JToggleButton{
    private int numero;
    public BtnPeca(int numero) {
        this.numero = numero;
        setSize(15, 15);
    }    

    public void Show() {
        setSelected(true);
        setText(Integer.toString(numero));
    }

    public void Hide(){
        setSelected(false);
        setText("");
    }

    public int getNumero() {
        return numero;
    }
}
