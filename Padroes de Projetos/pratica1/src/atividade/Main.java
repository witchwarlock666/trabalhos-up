package atividade;

public class Main {
	public static void main(String[] args) {
		Motocicleta v = new Motocicleta("Aaaa", "aa", 2020, 1000.00, 200);
		BancoDeDadosArmazenamento banco = new BancoDeDadosArmazenamento();
		banco.adicionarVeiculo(v);
		banco.recuperarInfo();
		
		//ArquivoArmazenamento arquivo = new ArquivoArmazenamento();
		//arquivo.adicionarVeiculo(v);
		//arquivo.adicionarVeiculo(v);
		//arquivo.adicionarVeiculo(v);
		//arquivo.adicionarVeiculo(v);
		//arquivo.recuperarInfo();
	}
}
