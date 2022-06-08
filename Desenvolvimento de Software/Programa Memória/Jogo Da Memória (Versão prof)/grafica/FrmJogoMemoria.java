// Felipe Lacerda E Fabricio Bertoncelo
// eu desisto dessa merda quero entrega assim msm e fodase, chega
package grafica;

import javax.swing.JFrame;

import logica.JogoMemoria;

import java.awt.GridLayout;

import java.awt.Dimension;

public class FrmJogoMemoria extends JFrame{
    
    BtnPeca[][] tabuleiro;
    JogoMemoria jogo;
    public FrmJogoMemoria() {
        tabuleiro = new BtnPeca[4][4];
        jogo = new JogoMemoria();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(4, 4, 10, 10));
        carregarPecas();
        setSize(new Dimension(300, 300));   
    }

    private void carregarPecas() {
        ActionBTN action = new ActionBTN(tabuleiro, jogo);
     
        for (int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                int numeroSorteado = jogo.getTabuleiro()[i][j];
                BtnPeca btn = new BtnPeca(numeroSorteado);
                tabuleiro[i][j] = btn;
                add(btn);
                btn.addActionListener(action);
            }
        }
    }

    public void mostrarTabuleiro(){
        for(int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                tabuleiro[i][j].Show();
            }
        }
    }

    public void ocultarTabuleiro(){
        for(int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                tabuleiro[i][j].Hide();
            }
        }
    }

}