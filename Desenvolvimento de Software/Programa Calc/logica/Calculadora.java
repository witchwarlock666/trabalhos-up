//Fabricio Bertoncello Filho e Felipe Lacerda

package logica;

public class Calculadora {

    public enum Operacao {
        SOMA,
        SUBTRACAO,
        MULTIPLICACAO,
        DIVISAO,
        POTENCIA;
    };

    private double operando1;
    private double operando2;
    private Operacao operacao;

    public double getOperando1() {
        return operando1;
    }

    public double getOperando2() {
        return operando2;
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

    public void setOperacao(Operacao operacao) {
        this.operacao = operacao;
    }

    public void setOperacao(int op) {
        operacao = Operacao.values()[op];
    }

    public double calcular() {

        switch (operacao) {
            case SOMA:
                return operando1 + operando2;
            case SUBTRACAO:
                return operando1 - operando2;
            case MULTIPLICACAO:
                return operando1 * operando2;
            case DIVISAO:
                return operando1 / operando2;
            default:
                return Math.pow(operando1, operando2);
        }
    }
}
