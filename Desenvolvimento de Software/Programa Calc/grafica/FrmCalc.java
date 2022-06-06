// Fabricio Bertoncelo e Felipe Lacerda
package grafica;

import javax.swing.AbstractAction;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import logica.Calculadora;

import javax.swing.*;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;

public class FrmCalc extends JFrame {
    private JTextField jTextFieldx;
    private JTextField jTextFieldy;
    private Calculadora calculadora;
    private double cataValorFInal;

    public FrmCalc() {

        this.calculadora = new Calculadora();

        setLayout(new BorderLayout());
        // criando o Jpanel
        JPanel pnl = new JPanel(new GridLayout(3, 2, 5, 5));
        this.add(pnl);
        // criando os jtextfields --
        this.jTextFieldx = new JTextField();
        pnl.add(this.jTextFieldx);
        this.jTextFieldx.setEditable(true);
        this.jTextFieldy = new JTextField();
        pnl.add(this.jTextFieldy);
        this.jTextFieldy.setEditable(true);

        String operacao[] = { "Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)", "Potenciação(a^b)" };
        JComboBox cb = new JComboBox(operacao);
        pnl.add(cb);

        JButton btn = new JButton("Calcular");
        btn.addActionListener(new AbstractAction() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    String txtAntigo = jTextFieldx.getText();
                    calculadora.setOperando1(Double.parseDouble(txtAntigo.replace(",", ".")));
                    String txtAntigo2 = jTextFieldy.getText();
                    calculadora.setOperando2(Double.parseDouble(txtAntigo2.replace(",", ".")));
                    calculadora.setOperacao(cb.getSelectedIndex());
                    cataValorFInal = calculadora.calcular();
                    Object[] options = { "OK" };
                    JOptionPane.showOptionDialog(null,
                            "Sua conta solicitada deu: " + cataValorFInal,
                            "Aviso",
                            JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE,
                            null, options, options[0]);
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(null, "Valor inválido para a operação! \n OBS: digite um número válido", "ERRO", JOptionPane.ERROR_MESSAGE);
                }

            }
        });
        pnl.add(btn);

        this.pack();
        this.setLocationRelativeTo(null);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }

}
