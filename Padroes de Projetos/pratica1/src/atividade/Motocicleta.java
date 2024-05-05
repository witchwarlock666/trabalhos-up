package atividade;

import java.util.ArrayList;
import java.util.List;

public class Motocicleta extends Veiculo {
    public int cilindradas;

    public Motocicleta(String marca, String modelo, int ano, double preco, int cilindradas) {
        super(marca, modelo, ano, preco);
        this.cilindradas = cilindradas;
    }
    
    public List<String> getSqlQueries() {
    	List<String> list = new ArrayList<String>();
    	list.add(String.format("insert into estoque (marca, modelo, ano, preco) values ('%s', '%s', '%d', '%f')", marca, modelo, ano, preco));
    	list.add(String.format("insert into adicionais (idestoque, titulo, valor) values (???, 'Cilindradas', '%d')", cilindradas));
        return list;
    }
    
    public String getFileOut() {
    	return String.format("Marca: %s\nModelo: %s\nAno: %d\nPreço: %f\nCilindradas: %d\n", this.marca, this.modelo, this.ano, this.preco, this.cilindradas);
    }
}
