package logica;

public class Calculadora {

     public ENUM Operacao {
            SOMA,
            SUBTRACAO,
            MULTIPLICACAO,
            DIVISAO,
            POTENCIA;
     }

    private double operando1;
    private double operando2;
    private boolean aguardando;
    private Operacao operacao;

    public double getOperando1() {
        return operando1;
    }

    public double getOperando2() {
        return operando2;
    }

    public boolean isAguardando() {
        return aguardando;
    }

    public Operacao getOperacao() {
       return operacao;
    }

    public void setOperando1(double operando1) {
        this.operando1 = operando1;
    }

    public void setOperando2(double operando2) {
        this.operando2 = operando2;
    }
    public void setAguardando(boolean aguardando) {
        this.aguardando = aguardando;
    }
    
     public void setOperacao(Operacao operacao) {
         this.operacao = operacao;
     }

    public double calcular(Double p1, Double p2, int operacao) {

        switch (operacao) {
            case 0: return p1 + p2;
            case 1: return p1 - p2;
            case 2: return p1 * p2;
            case 3: return p1 / p2;
            default: return Math.pow(p1, p2);
        }
    }
}

