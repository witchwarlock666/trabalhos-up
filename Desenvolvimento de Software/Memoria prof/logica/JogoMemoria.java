//Fabricio Bertoncello Filho e Felipe Lacerda

package logica;

import java.util.Random;

import grafica.BtnPeca;

public class JogoMemoria {
    private int[][] tabuleiro;
    private int pontuacao;
    private boolean aguardandoPeca;
    private BtnPeca pecaSelecionada;
    private int i1, j1;
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

    public void givePoint(){
        pontuacao += 5;
    }

    public void takePoint(){
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

    public void setIJ(int i, int j) {
        i1 = i;
        j1 = j;
    }

    public boolean checkSame(int i2, int j2) {
        if (i1 == i2 && j1 == j2) {
            return true;
        }
        else {
            return false;
        }
    }
}
