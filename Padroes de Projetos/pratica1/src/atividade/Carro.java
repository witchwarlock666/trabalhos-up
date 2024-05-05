package atividade;

import java.util.ArrayList;
import java.util.List;

public class Carro extends Veiculo {
    public int numeroPortas;

    public Carro(String marca, String modelo, int ano, double preco, int numeroPortas) {
        super(marca, modelo, ano, preco);
        this.numeroPortas = numeroPortas;
    }
    
    public List<String> getSqlQueries() {
    	List<String> list = new ArrayList<String>();
    	list.add(String.format("insert into estoque (marca, modelo, ano, preco) values ('%s', '%s', '%d', '%f')", marca, modelo, ano, preco));
    	list.add(String.format("insert into adicionais (idestoque, titulo, valor) values (???, 'Numero de Portas', '%d')", numeroPortas));
        return list;
    }
    
    public String getFileOut() {
    	return String.format("Marca: %s\nModelo: %s\nAno: %d\nPreço: %f\nNumero de Portas: %d\n", this.marca, this.modelo, this.ano, this.preco, this.numeroPortas);
    }
}
