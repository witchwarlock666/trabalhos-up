package grafica;

import java.awt.event.ActionEvent;

import javax.swing.AbstractAction;
import javax.swing.JOptionPane;

import logica.JogoMemoria;

public class ActionConferir extends AbstractAction {
    BtnPeca[][] tabuleiro;
    private JogoMemoria memoria;

    public ActionConferir(BtnPeca[][] tabuleiro, JogoMemoria memoria) {
        this.tabuleiro = tabuleiro;
        this.memoria = memoria;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        BtnPeca btn = (BtnPeca) e.getSource();
        int numero = btn.getNumero();
        if (memoria.isAguardandoPeca()) {
            if (!memoria.checkSame(btn.i, btn.j)) {
                // fazer a conferencia
                if (numero == memoria.getPecaSelecionada().getNumero()) {
                    // acertou
                    memoria.givePoint();
                    memoria.setAguardandoPeca(false);
                    btn.mostrar();
                    if (verificarFim()) {
                        // fim de jogo
                        JOptionPane.showMessageDialog(null, String.format("Pontuação final %d", memoria.getPontuacao()),
                                "jogo da memória", JOptionPane.INFORMATION_MESSAGE);
                        ;
                    }
                    btn.setEnabled(false);
                    memoria.getPecaSelecionada().setEnabled(false);
                } else {
                    // errou
                    memoria.takePoint();
                    memoria.setAguardandoPeca(false);
                    // desvira as duas peças
                    btn.ocultar();
                    memoria.getPecaSelecionada().ocultar();
                }
            }
        } else {
            memoria.setIJ(btn.i, btn.j);
            memoria.setPecaSelecionada(btn);
            memoria.setAguardandoPeca(true);
            btn.mostrar();
        }
    }

    private boolean verificarFim() {
        int cont = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (tabuleiro[i][j].isSelected()) {
                    cont++;
                }
            }
        }
        if (cont == 16) {
            return true;
        } else {
            return false;
        }

    }
}
