// Felipe Lacerda E Fabricio Bertoncelo
package logica;

import java.util.Random;

import grafica.BtnPeca;

public class JogoMemoria {
    private int[][] tabuleiro;
    private int pontuacao;
    private boolean aguardandoPeca;
    private BtnPeca pecaSelecionada;
    public JogoMemoria(){
        tabuleiro = new int[4][4];
        for (int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                tabuleiro[i][j] = sortearNumero();
            }
        }
    }
    private int sortearNumero() {
        while(true){
            int numeroSorteado = new Random().nextInt(8) + 1;
            int cont = 0;
            for(int i = 0; i < 4; i++){
                for(int j = 0; j < 4; j++){
                    if(numeroSorteado == tabuleiro[i][j]){
                        cont++;
                    }
                }
            }
            if(cont < 2){
                return numeroSorteado;
            }
        }
    }

    public int[][] getTabuleiro() {
        return tabuleiro;
    }

    public int getPontuacao() {
        return pontuacao;
    }

    public void aumentarPontuacao(){
        pontuacao += 5;
    }

    public void diminuirPontuacao(){
        pontuacao -= 3;
    }

    public boolean isAguardandoPeca() {
        return aguardandoPeca;
    }

    public void setAguardandoPeca(boolean aguardandoPeca) {
        this.aguardandoPeca = aguardandoPeca;
    }

    public void setPecaSelecionada(BtnPeca pecaSelecionada) {
        this.pecaSelecionada = pecaSelecionada;
    }

    public BtnPeca getPecaSelecionada() {
        return pecaSelecionada;
    }
}
