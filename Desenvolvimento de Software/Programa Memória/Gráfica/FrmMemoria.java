package Gráfica;

import javax.swing.JFrame;
import javax.swing.JToggleButton;

import Lógica.Memoria;

import java.awt.GridLayout;
import java.awt.event.ItemEvent;

public class FrmMemoria extends JFrame {

    private JToggleButton button;
    public Memoria memoria = new Memoria();

    public FrmMemoria() {
        super("Jogo da memoria");
        this.setBounds(200, 100, 500, 300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        memoria.gerarNumeros();
        setJToggleButton();
        this.setLayout(new GridLayout(4, 4, 10, 10));

    }

    private void setJToggleButton() {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int num = memoria.getNum(i, j);
                String n = Integer.toString(num);
                button = new JToggleButton(n);
                add(button);
                button.addActionListener(new ActionBotao(num, false));
            }
        }
    }

    public void itemStateChanged(ItemEvent eve) {
        if (button.isSelected())
            button.setText("OFF");
        else
            button.setText("ON");
    }
}
