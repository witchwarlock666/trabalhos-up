
//n tenho a menor ideia doq eu to fazendo

package Gráfica;

import javax.swing.JFrame;
import java.awt.FlowLayout;  
import java.awt.event.ItemEvent;     
import javax.swing.JToggleButton;




public class FrmMemoria extends JFrame{
   
    private JToggleButton button; 

    public FrmMemoria(){
        super("Memory Game");
        this.setBounds(200, 100, 500, 300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setJToggleButton();  
        setLayout(new FlowLayout());  

     }

     private void setJToggleButton() {  
        button = new JToggleButton("ON"); 
        //button.addActionListener(new java.awt.event.ActionListener() {
           //@Override
           // public void actionPerformed(java.awt.event.ActionEvent evt) {
                
            //}
        //});
        add(button);
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button);   
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
        button = new JToggleButton("ON");  
        add(button); 
    }  
        
        public void itemStateChanged(ItemEvent eve) {  
        if (button.isSelected())  
            button.setText("OFF");  
        else  
            button.setText("ON");  
    }
}    
  
 