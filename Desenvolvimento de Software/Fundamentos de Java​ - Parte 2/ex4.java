import java.util.Scanner;



public class ex4 {

 public static void main(String args[]) {
    Scanner catador = new Scanner(System.in);
    
    int x;
    int i, j;
    int resulty, resultya;
    resulty = 0;
    resultya = 0;
    int[] a = new int[100];
    
    System.out.println("Digite o x: ");
    x = catador.nextInt();
    System.out.println("Digite o i: ");
    j = catador.nextInt();

    if(  j <=0 || x <= 0  ){
        System.out.println("Valor inválido");
    }
    
    else{
        for(i = j;i>0; i--){
            System.out.printf("Digite o A de posição %d: ", a);
            a[i] = catador.nextInt(); 
           
        }
        for(i = j; i>0 ; i--){
        resulty += (int) a[i]*Math.pow(x, i);
        System.out.printf(" Resultado da equação de Y (ausência de N): %d", resulty);

        for(i = j; i>0 ; --i){
        resultya += (int)i * a[i]*Math.pow(x, i);
        System.out.printf(" Resultado da equação de Y (ausência de N): %d", resultya);
        }
        
    }
}
}
}

