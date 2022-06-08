// Felipe Lacerda E Fabricio Bertoncelo
package grafica;

import java.awt.event.ActionEvent;


import javax.swing.AbstractAction;
import javax.swing.JOptionPane;

import logica.JogoMemoria;

public class ActionBTN extends AbstractAction {
    BtnPeca [][] tabuleiro;
    private JogoMemoria jogo;
    // private boolean apertou;
  

    public ActionBTN(BtnPeca[][] tabuleiro, JogoMemoria jogo){
        this.tabuleiro = tabuleiro;
        this.jogo = jogo;
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        BtnPeca btn = (BtnPeca) e.getSource();
        int numero = btn.getNumero();
        if(jogo.isAguardandoPeca()) {
           
            if(numero == jogo.getPecaSelecionada().getNumero()){
                jogo.aumentarPontuacao();
                jogo.setAguardandoPeca(false);
                btn.Show();
                // apertou = true;
                if(verificarFim()){
                    JOptionPane.showMessageDialog(null, String.format("Pontuação final %d", jogo.getPontuacao()), "jogo da memória", JOptionPane.INFORMATION_MESSAGE);;
                }
                btn.setEnabled(false);
                jogo.getPecaSelecionada().setEnabled(false);
                    //  if(apertou){
                    //         JOptionPane.showMessageDialog(null, String.format("Não vale apertar o mesmo botão duas vezes!! "), "Alerta!!!", JOptionPane.ERROR_MESSAGE);
                    //         jogo.diminuirPontuacao();
                    //         jogo.setAguardandoPeca(false);
                    //         btn.ocultar();
                    //         apertou = false;
                    //         btn.setEnabled(false);
                    //      }
            }else{
                jogo.diminuirPontuacao();
                jogo.setAguardandoPeca(false);
                btn.Hide();
               
            }
        }else{
            jogo.setPecaSelecionada(btn);
            jogo.setAguardandoPeca(true);
            btn.Show();
        }
    }

    private boolean verificarFim(){
        int cont = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if (tabuleiro[i][j].isSelected()){
                    cont++;
                }
            }
        }
        if(cont == 16){
            return true;
        }else{
            return false;
        }
        
    }
}
