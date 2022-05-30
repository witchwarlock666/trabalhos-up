
package Lógica;
//import java.util.Random;

import java.util.Random;

public class Memoria{

    public int[][] numeros = new int[4][4];

    public Memoria(){
    }
    
    public void gerarNumeros() {

        int nums[] = {2,2,2,2,2,2,2,2};

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                Random rand = new Random();
                int val = rand.nextInt(8);

                if (nums[val] != 0) {
                    nums[val]--;
                    numeros[i][j] = val + 1;
                }
                else {
                    j--;
                }
            }
        }
    }

    public int getNum(int i, int j) {
        return numeros[i][j];
    }

 }
    