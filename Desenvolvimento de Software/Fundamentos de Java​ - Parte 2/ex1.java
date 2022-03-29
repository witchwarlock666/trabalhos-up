// Exercício feito por Fabrício e Felipe
import java.util.Scanner;


public class teste {


 public static void main(String args[]) {




  Scanner myObj = new Scanner(System.in);


  int acumulo;


  System.out.println("Olá, digite o número desejado para fatorial: ");


  int x = myObj.nextInt();

  int i;




  acumulo = 1;




 if(x>0) {




  for(i=x; i>0; i--) {




  acumulo = acumulo * i;




 }




 System.out.print("Fatorial de "+ x );

 System.out.println("\n e  " + acumulo);





 }




 else {




 System.out.print("Impossível realizar conta, x<0.");




 }


 }

} 
