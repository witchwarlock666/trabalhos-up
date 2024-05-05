package atividade;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;

public class BancoDeDadosArmazenamento implements Armazenamento {

    @Override
    public void adicionarVeiculo(Veiculo veiculo) {
    	Connection conn = null;
    	try {
		    conn = DriverManager.getConnection("jdbc:mysql://localhost/pratica1?" +
		                                "user=root&password=f90100600");
		    
		    List<String> queries = veiculo.getSqlQueries();
		    
		    Statement st = conn.prepareStatement(queries.get(0));
	    	st.execute(queries.get(0));
	    	
	    	st = conn.prepareStatement("select idestoque from estoque order by idestoque desc");
	    	ResultSet res = st.executeQuery("select idestoque from estoque order by idestoque desc");
	    	res.next();
	    	int id = res.getInt(1);
	    	
	    	
		    
		    for (int i = 1; i < queries.size(); i++) {
		    	String q = queries.get(i).replace("???", Integer.toString(id));
		    	st = conn.prepareStatement(q);
		    	st.execute(q);
		    }
		    
		    
		} catch (SQLException ex) {
		    //Caso ocorram erros na tentativa de conexão com o MySQL
		    System.out.println("SQL Exception: " + ex.getMessage());
		    System.out.println("Código do erro: " + ex.getErrorCode());
		}
    }

    @Override
    public void recuperarInfo() {
    	Connection conn = null;
    	try {
		    conn = DriverManager.getConnection("jdbc:mysql://localhost/pratica1?" +
		                                "user=root&password=f90100600");
		    
		    Statement st = conn.prepareStatement("select * from estoque");
	    	ResultSet res = st.executeQuery("select * from estoque");
	    	
	    	while (res.next()) {
	    		int id = res.getInt(1);
	    		String marca = res.getNString(2);
	    		String modelo = res.getNString(3);
	    		int ano = res.getInt(4);
	    		double preco = res.getDouble(5);
	    		
	    		System.out.println(String.format("Marca: %s", marca));
	    		System.out.println(String.format("Modelo: %s", modelo));
	    		System.out.println(String.format("Ano: %d", ano));
	    		System.out.println(String.format("Preço: %.2f", preco));
	    		
	    		st = conn.prepareStatement(String.format("select titulo, valor from adicionais where idestoque = %d", id));
	    		ResultSet res2 = st.executeQuery(String.format("select titulo, valor from adicionais where idestoque = %d", id));
	    		
	    		while (res2.next()) {
		    		System.out.println(String.format("%s: %s", res2.getNString(1), res2.getNString(2)));
	    		}

	    		System.out.println("");
	    	}
		    
		    
		} catch (SQLException ex) {
		    //Caso ocorram erros na tentativa de conexão com o MySQL
		    System.out.println("SQL Exception: " + ex.getMessage());
		    System.out.println("Código do erro: " + ex.getErrorCode());
		}
    }
    
}
