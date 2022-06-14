//Fabricio Bertoncello Filho e Felipe Lacerda

package grafica;

import javax.swing.JFrame;

import logica.JogoMemoria;

import java.awt.GridLayout;

import java.awt.Dimension;

public class FrmJogoMemoria extends JFrame{
    
    BtnPeca[][] pecas;
    JogoMemoria memoria;
    public FrmJogoMemoria() {
        pecas = new BtnPeca[4][4];
        memoria = new JogoMemoria();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(4, 4, 10, 10));
        carregarPecas();
        setSize(new Dimension(300, 300));   
    }

    private void carregarPecas() {
        //vincular action ao botao
        ActionConferir action = new ActionConferir(pecas, memoria);
     
        for (int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                int n = memoria.getTabuleiro()[i][j];
                BtnPeca btn = new BtnPeca(n, i, j);
                pecas[i][j] = btn;
                add(btn);
                btn.addActionListener(action);
            }
        }
    }

    public void mostrarTabuleiro(){
        for(int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                pecas[i][j].mostrar();
            }
        }
    }

    public void ocultarTabuleiro(){
        for(int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                pecas[i][j].ocultar();
            }
        }
    }

}