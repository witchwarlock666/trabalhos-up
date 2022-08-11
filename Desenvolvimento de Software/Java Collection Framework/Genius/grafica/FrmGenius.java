package grafica;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

import logica.Genius;
import logica.Genius.Cor;

import java.awt.GridLayout;
import java.awt.Dimension;
import java.awt.Color;

public class FrmGenius extends JFrame {

    private Genius logicaGenius;

    private JButton btnRed;
    private JButton btnGreen;
    private JButton btnBlue;
    private JButton btnYellow;

    public FrmGenius(Genius logicaGenius) {
        this.logicaGenius = logicaGenius;

        this.setLayout(new GridLayout(2, 2, 10, 10));

        btnRed = new JButton();
        btnRed.setMinimumSize(new Dimension(50, 50));
        btnRed.setBackground(Color.RED);
        this.add(btnRed);

        btnGreen = new JButton();
        btnGreen.setMinimumSize(new Dimension(50, 50));
        btnGreen.setBackground(Color.GREEN);
        this.add(btnGreen);

        btnBlue = new JButton();
        btnBlue.setMinimumSize(new Dimension(50, 50));
        btnBlue.setBackground(Color.BLUE);
        this.add(btnBlue);

        btnYellow = new JButton();
        btnYellow.setMinimumSize(new Dimension(50, 50));
        btnYellow.setBackground(Color.YELLOW);
        this.add(btnYellow);

        this.pack();
        this.setSize(600, 600);
        this.setLocationRelativeTo(null);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        btnRed.addActionListener(new ActionBotao(Cor.RED, logicaGenius));
        btnGreen.addActionListener(new ActionBotao(Cor.GREEN, logicaGenius));
        btnBlue.addActionListener(new ActionBotao(Cor.BLUE, logicaGenius));
        btnYellow.addActionListener(new ActionBotao(Cor.YELLOW, logicaGenius));
    }

    public void animarBotoes() {
        ThreadAnimacoesBotoes animacao = new ThreadAnimacoesBotoes(btnRed, btnGreen, btnBlue, btnYellow, logicaGenius);
        animacao.run();
    }

    public void sortear() {
        logicaGenius.sortearCor();
    }
}
