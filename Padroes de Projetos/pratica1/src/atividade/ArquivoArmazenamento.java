package atividade;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Scanner;


public class ArquivoArmazenamento implements Armazenamento {

    @Override
    public void adicionarVeiculo(Veiculo veiculo) {
    	try {
    		File file = new File("Estoque");
    		file.createNewFile();
    		
    		FileWriter writer = new FileWriter("Estoque", true);
    		writer.append(veiculo.getFileOut());
    		writer.append(" \n");
    		
    		writer.close();
    	} catch (IOException e) {
    		System.out.println("Write Exception: " + e.getMessage());
    	}
    	//String str = veiculo.getFileOut();
        //BufferedWriter writer = new BufferedWriter(new FileWriter("./src/atividade/Estoque", true));
        //writer.append(str);
        //writer.append('\n');
        
        //writer.close();
    }

    @Override
    public void recuperarInfo() {
    	try {
    	      File file = new File("Estoque");
    	      Scanner scanner = new Scanner(file);
    	      
    	      while (scanner.hasNextLine()) {
    	        String data = scanner.nextLine();
    	        System.out.println(data);
    	      }
    	      
    	      scanner.close();
    	    } catch (FileNotFoundException e) {
        		System.out.println("Read Exception: " + e.getMessage());
    	    }
    }
    
}
