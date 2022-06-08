// Felipe Lacerda E Fabricio Bertoncelo
package logica;

import grafica.FrmJogoMemoria;

public class Main {
    public static void main(String[] args) {
        FrmJogoMemoria frm = new FrmJogoMemoria();
        frm.setVisible(true);
        frm.mostrarTabuleiro();
        try{
            Thread.sleep(5000);
        }catch (InterruptedException ex){
            ex.printStackTrace();
        }
        frm.ocultarTabuleiro();
    }
}
