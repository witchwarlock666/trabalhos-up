package grafica;

import javax.swing.AbstractAction;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import logica.Calculadora;
// import logica.Calculadora.Operacao;

import javax.swing.*;
//import logica.Calculadora.Operacao;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;


public class FrmCalc extends JFrame {
    private JTextField jTextFieldx;
    private JTextField jTextFieldy;
    private Calculadora calculadora;
    //private JOptionPane DropDown;
    private double cataValorFInal;
    public FrmCalc() {
       
        this.calculadora = new Calculadora();

        setLayout(new BorderLayout());
        //criando o Jpanel
        JPanel pnl = new JPanel(new GridLayout(3, 2, 5, 5));
        this.add(pnl);
        // criando os jtextfields --
        this.jTextFieldx = new JTextField();
        pnl.add(this.jTextFieldx);
        this.jTextFieldx.setEditable(true);
        this.jTextFieldy = new JTextField();
        pnl.add(this.jTextFieldy);
        this.jTextFieldy.setEditable(true);
     

       
        // // JPanel pnlCentro = new JPanel(new GridLayout(5, 4, 5, 5));
        // // this.add(pnlCentro, BorderLayout.CENTER);

        // JButton btn = new JButton("C");
       

        // btn = new JButton("*");
        // btn.addActionListener(new AbstractAction() {
        //     @Override
        //     public void actionPerformed(ActionEvent e) {                
        //         String txtAntigo = txtDisplay.getText();
        //         calculadora.setOperando1(Double.parseDouble(txtAntigo.replace(",", ".")));
        //         calculadora.setOperacao(Operacao.MULTIPLICACAO);
        //         calculadora.setAguardando(true);
        //         txtDisplay.setText("");
        //     }
        // });            
        // // pnlCentro.add(btn);

        // btn = new JButton("<html>a<sup>b</sup></html>");
        // btn.addActionListener(new AbstractAction() {
        //     @Override
        //     public void actionPerformed(ActionEvent e) {                
        //         String txtAntigo = txtDisplay.getText();
        //         calculadora.setOperando1(Double.parseDouble(txtAntigo.replace(",", ".")));
        //         calculadora.setOperacao(Operacao.POTENCIA);
        //         calculadora.setAguardando(true);
        //         txtDisplay.setText("");
        //     }
        // });            
        // // pnlCentro.add(btn);

       

       
        // btn = new JButton("/");
        // btn.addActionListener(new AbstractAction() {
        //     @Override
        //     public void actionPerformed(ActionEvent e) {                
        //         String txtAntigo = txtDisplay.getText();
        //         calculadora.setOperando1(Double.parseDouble(txtAntigo.replace(",", ".")));
        //         calculadora.setOperacao(Operacao.DIVISAO);
        //         calculadora.setAguardando(true);
        //         txtDisplay.setText("");
        //     }
        // });            
        // // pnlCentro.add(btn);


        // btn = new JButton("+");
        // btn.addActionListener(new AbstractAction() {
        //     @Override
        //     public void actionPerformed(ActionEvent e) {                
        //         String txtAntigo = txtDisplay.getText();
        //         calculadora.setOperando1(Double.parseDouble(txtAntigo.replace(",", ".")));
        //         calculadora.setOperacao(Operacao.SOMA);
        //         calculadora.setAguardando(true);
        //         txtDisplay.setText("");
        //     }
        // });   
        // // pnlCentro.add(btn);


        // btn = new JButton("-");
        // btn.addActionListener(new AbstractAction() {
        //     @Override
        //     public void actionPerformed(ActionEvent e) {                
        //         String txtAntigo = txtDisplay.getText();
        //         calculadora.setOperando1(Double.parseDouble(txtAntigo.replace(",", ".")));
        //         calculadora.setOperacao(Operacao.SUBTRACAO);
        //         calculadora.setAguardando(true);
        //         txtDisplay.setText("");
        //     }
        // });            
        // // pnlCentro.add(btn);

        // btn = new JButton("+/-");
        // btn.addActionListener(new AbstractAction() {
        //     @Override
        //     public void actionPerformed(ActionEvent e) {
        //         String txtAntigo = txtDisplay.getText();
        //         double num = Double.parseDouble(txtAntigo.replace(",", "."));
        //         num *= -1; // num = -1 * num
        //         txtDisplay.setText(String.format("%f", num));
        //     }
        // });
        // // pnlCentro.add(btn);

        String operacao[]={"Multiplicação (*)", "Divisão (/)", "Soma (+)", "Subtração (-)", "Potenciação(a^b)"};        
        JComboBox cb = new JComboBox(operacao);
        pnl.add(cb);

       JButton btn = new JButton("=");
        btn.addActionListener(new AbstractAction() {
            @Override
            public void actionPerformed(ActionEvent e) { 
                if(calculadora.isAguardando()){
                    String txtAntigo = jTextFieldx.getText();
                    calculadora.setOperando1(Double.parseDouble(txtAntigo.replace(",", ".")));
                    String txtAntigo2 = jTextFieldy.getText();
                    calculadora.setOperando2(Double.parseDouble(txtAntigo.replace(",", ".")));
                    calculadora.calcular(p1, p2) cb.getItemAt(cb.getSelectedIndex());
                    cataValorFInal = calculadora.calcular(Double.parseDouble(txtAntigo), Double.parseDouble(txtAntigo2));
                    
                }  
                      
              
                    
            }
        });
        pnl.add(btn);

    
        
        // Arrumar o retorno de conta, é só colocar dentro do action listener pra linkar o JComboBox com o método da outra clase("Calcular")
            





        if(calculadora.isAguardando()){
            Object[] options = { "SIM", "NÃO"};
        JOptionPane.showOptionDialog(null, "Sua conta solicitada deu: " + cataValorFInal + "\n Deseja Continuar?", "Aviso",
          JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE,
              null, options, options[0]);
              calculadora.setAguardando(false);
            }
            
        
        this.pack();
        this.setLocationRelativeTo(null);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    
        }  
        
       
     
          
           
}
