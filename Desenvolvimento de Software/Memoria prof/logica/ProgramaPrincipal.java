//Fabricio Bertoncello Filho e Felipe Lacerda

package logica;

import grafica.FrmJogoMemoria;

public class ProgramaPrincipal {
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
