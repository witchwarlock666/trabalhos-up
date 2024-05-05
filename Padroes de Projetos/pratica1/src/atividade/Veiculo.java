package atividade;

import java.util.ArrayList;
import java.util.List;

public class Veiculo {
    public String marca;
    public String modelo;
    public int ano;
    public double preco;
    
    public Veiculo() {}

    public Veiculo(String marca, String modelo, int ano, double preco) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.preco = preco;
    }

    public List<String> getSqlQueries() {
    	List<String> list = new ArrayList<String>();
    	list.add(String.format("insert into estoque (marca, modelo, ano, preco) values ('%s', '%s', '%d', '%f')", marca, modelo, ano, preco));
        return list;
    }
    
    public String getFileOut() {
    	return String.format("Marca: %s\nModelo: %s\nAno: %d\nPreço: %f\n", this.marca, this.modelo, this.ano, this.preco);
    }
}
