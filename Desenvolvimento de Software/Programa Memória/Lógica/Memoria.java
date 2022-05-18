package Lógica;

import java.util.Random;

public class Memoria{
    public static void main(String[] args) {
        int catador[][] = new int[2][2];
        int copiaCatador[][] = new int[2][2];    
    int i, j;
    Random aleatorio = new Random();
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
           catador[i][j] = aleatorio.nextInt(101);
        }
    }
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
    System.out.println(catador[i][j]);
        }
    }
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            copiaCatador[i][j] = catador[i][j];
        }
    }
    System.out.println("************Cópia*********");
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            System.out.println(copiaCatador[i][j]);
    }

}

}
}
    