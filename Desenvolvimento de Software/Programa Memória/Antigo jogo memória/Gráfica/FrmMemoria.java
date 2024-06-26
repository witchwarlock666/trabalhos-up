package Gráfica;

import javax.swing.JFrame;
import javax.swing.JToggleButton;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.JOptionPane;

import Lógica.Memoria;

import java.awt.GridLayout;



public class FrmMemoria extends JFrame {

    private JToggleButton btn1;
    private JToggleButton btn2;
    private JToggleButton btn3;
    private JToggleButton btn4;
    private JToggleButton btn5;
    private JToggleButton btn6;
    private JToggleButton btn7;
    private JToggleButton btn8;
    private JToggleButton btn9;
    private JToggleButton btn10;
    private JToggleButton btn11;
    private JToggleButton btn12;
    private JToggleButton btn13;
    private JToggleButton btn14;
    private JToggleButton btn15;
    private JToggleButton btn16;
    private boolean selection;
    private Memoria memoria = new Memoria();
    private JToggleButton[][] botoes;
    private int num;
    private String[] n = new String[16];

    public FrmMemoria() {
        super("Jogo da memoria");
        botoes = new JToggleButton[4][4];
        //setBotoes();
        this.setBounds(200, 100, 500, 300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        memoria.gerarNumeros();
        setJToggleButton();
        this.setLayout(new GridLayout(4, 4, 10, 10));

    }
    private void setWarnings(){
        if(memoria.IsFinished && memoria.inPlay){
            JOptionPane.showMessageDialog(null, "Parabéns, você acertou!",
            "Parabéns!!!", JOptionPane.INFORMATION_MESSAGE);
        }

    }


    public void setJToggleButton(){

  
        // for (int i = 0; i < 4; i++) {
        // for (int j = 0; j < 4; j++) {
        // int num = memoria.getNum(i, j);
        // String n = Integer.toString(num);
        // button = new JToggleButton(n);
        // botoes[i][j] = button;
        // add(button);
        // button.addChangeListener(new ChangeListener() {
        // @Override
        // public void stateChanged(ChangeEvent event) {
        // if (button.isSelected()){
        // button.setText("ON");
        // } else {
        // button.setText("OFF");
        // }
        // }
        // });
        // }
        // }
    
        /*Arrumemo, tem que disselecionar o botão depois da primeira verificação, só que não sei como colocar um timer 
        antes da deceleção  pra pode fica aparecendo o número  ai n sei comeq faz essa bagunça.*/
        num = memoria.getNum(0, 0);
        n[0] = Integer.toString(num);
        btn1 = new JToggleButton();
        add(btn1);
        btn1.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                //public void run(){
                    if(selection){
                        //Thread.sleep(5000);
                        btn1.setSelected(false);
    
                    }    
                    if (btn1.isSelected()) {
                            btn1.setText(n[0]);
                            if(memoria.getInPlay()){
                                memoria.setSecond(Integer.parseInt(n[0]));
                                memoria.setIsFinished(true);
                                setWarnings();
        
                            } else{
                                memoria.setFirst(Integer.parseInt(n[0]));
                                memoria.setInPlay(true);
                            }
                            
                           selection = true;
        
                        } else {
                            btn1.setText("");
                        }  
                }
               // }
            });
    
               

    

        num = memoria.getNum(0, 1);
        n[1] = Integer.toString(num);
        btn2 = new JToggleButton();
        add(btn2);
        btn2.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn2.isSelected()) {
                    btn2.setText(n[1]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[1]));
                        memoria.setIsFinished(true);
                        setWarnings();
                        

                    } else{
                        memoria.setFirst(Integer.parseInt(n[1]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn2.setText("");
                }
            }
        });
        num = memoria.getNum(0, 2);
        n[2] = Integer.toString(num);
        btn3 = new JToggleButton();
        add(btn3);
        btn3.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn3.isSelected()) {
                    btn3.setText(n[2]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[2]));
                        memoria.setIsFinished(true);
                       

                    } else{
                        memoria.setFirst(Integer.parseInt(n[2]));
                        memoria.setInPlay(true);
                    }
                      
                } else {
                    btn3.setText("");
                }
            }
        });
        num = memoria.getNum(0, 3);
        n[3] = Integer.toString(num);
        btn4 = new JToggleButton();
        add(btn4);
        btn4.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn4.isSelected()) {
                    btn4.setText(n[3]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[3]));
                        memoria.setIsFinished(true);

                    } else{
                        memoria.setFirst(Integer.parseInt(n[3]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn4.setText("");
                }
            }
        });
        num = memoria.getNum(1, 0);
        n[4] = Integer.toString(num);
        btn5 = new JToggleButton();
        add(btn5);
        btn5.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn5.isSelected()) {
                    btn5.setText(n[4]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[4]));
                        memoria.setIsFinished(true);

                    } else{
                        memoria.setFirst(Integer.parseInt(n[4]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn5.setText("");
                }
            }
        });
        num = memoria.getNum(1, 1);
        n[5] = Integer.toString(num);
        btn6 = new JToggleButton();
        add(btn6);
        btn6.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn6.isSelected()) {
                    btn6.setText(n[5]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[5]));
                        memoria.setIsFinished(true);
                      

                    } else{
                        memoria.setFirst(Integer.parseInt(n[5]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn6.setText("");
                }
            }
        });
        num = memoria.getNum(1, 2);
        n[6] = Integer.toString(num);
        btn7 = new JToggleButton();
        add(btn7);
        btn7.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn7.isSelected()) {
                    btn7.setText(n[6]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[6]));
                        memoria.setIsFinished(true);
                        

                    } else{
                        memoria.setFirst(Integer.parseInt(n[6]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn7.setText("");
                }
            }
        });
        num = memoria.getNum(1, 3);
        n[7] = Integer.toString(num);
        btn8 = new JToggleButton();
        add(btn8);
        btn8.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn8.isSelected()) {
                    btn8.setText(n[7]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[7]));
                        memoria.setIsFinished(true);
                      

                    } else{
                        memoria.setFirst(Integer.parseInt(n[7]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn8.setText("");
                }
            }
        });
        num = memoria.getNum(2, 0);
        n[8] = Integer.toString(num);
        btn9 = new JToggleButton();
        add(btn9);
        btn9.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn9.isSelected()) {
                    btn9.setText(n[8]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[8]));
                        memoria.setIsFinished(true);
                        

                    } else{
                        memoria.setFirst(Integer.parseInt(n[8]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn9.setText("");
                }
            }
        });
        num = memoria.getNum(2, 1);
        n[9] = Integer.toString(num);
        btn10 = new JToggleButton();
        add(btn10);
        btn10.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn10.isSelected()) {
                    btn10.setText(n[9]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[9]));
                        memoria.setIsFinished(true);
                       

                    } else{
                        memoria.setFirst(Integer.parseInt(n[9]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn10.setText("");
                }
            }
        });
        num = memoria.getNum(2, 2);
        n[10] = Integer.toString(num);
        btn11 = new JToggleButton();
        add(btn11);
        btn11.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn11.isSelected()) {
                    btn11.setText(n[10]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[10]));
                        memoria.setIsFinished(true);
                        
                    } else{
                        memoria.setFirst(Integer.parseInt(n[10]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn11.setText("");
                }
            }
        });
        num = memoria.getNum(2, 3);
        n[11] = Integer.toString(num);
        btn12 = new JToggleButton();
        add(btn12);
        btn12.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn12.isSelected()) {
                    btn12.setText(n[11]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[11]));
                        memoria.setIsFinished(true);
                       

                    } else{
                        memoria.setFirst(Integer.parseInt(n[11]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn12.setText("");
                }
            }
        });
        num = memoria.getNum(3, 0);
        n[12] = Integer.toString(num);
        btn13 = new JToggleButton();
        add(btn13);
        btn13.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn13.isSelected()) {
                    btn13.setText(n[12]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[12]));
                        memoria.setIsFinished(true);
                        

                    } else{
                        memoria.setFirst(Integer.parseInt(n[12]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn13.setText("");
                }
            }
        });
        num = memoria.getNum(3, 1);
        n[13] = Integer.toString(num);
        btn14 = new JToggleButton();
        add(btn14);
        btn14.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn14.isSelected()) {
                    btn14.setText(n[13]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[13]));
                        memoria.setIsFinished(true);
                       

                    } else{
                        memoria.setFirst(Integer.parseInt(n[13]));
                        memoria.setInPlay(true);
                    }
                } else {
                    btn14.setText("");
                }
            }
        });

        num = memoria.getNum(3, 2);
        n[14] = Integer.toString(num);
        btn15 = new JToggleButton();
        add(btn15);
        btn15.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn15.isSelected()) {
                    btn15.setText(n[14]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[14]));
                        memoria.setIsFinished(true);
                       

                    } else{
                        memoria.setFirst(Integer.parseInt(n[14]));
                        memoria.setInPlay(true);
                    }
                    } else{
                    btn15.setText("");
                }
            
        }});

        num = memoria.getNum(3, 3);
        n[15] = Integer.toString(num);
        btn16 = new JToggleButton();
        add(btn16);
        btn16.addChangeListener(new ChangeListener(){
            @Override
            public void stateChanged(ChangeEvent event) {
                if (btn16.isSelected()) {
                    btn16.setText(n[15]);
                    if(memoria.getInPlay()){
                        memoria.setSecond(Integer.parseInt(n[15]));
                        memoria.setIsFinished(true);
                       

                    } else{
                        memoria.setFirst(Integer.parseInt(n[15]));
                        memoria.setInPlay(true);
                    
                    } 
                    } else {
                        btn16.setText("");
                    }
                }
            });
       
       
   
    
        }
        }
    
    // public void itemStateChanged(ItemEvent eve) {
    // if (button.isSelected())
    // button.setText("OFF");
    // else
    // button.setText("ON");
    // }

    // private void setBotoes() {

    // }
