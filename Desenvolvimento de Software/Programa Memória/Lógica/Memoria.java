
package Lógica;
//import java.util.Random;

import java.util.Random;

public class Memoria{

    public int[][] numeros = new int[4][4];
    public int first;
    public int second;
    public boolean inPlay;
    public boolean IsFinished;

    public Memoria(){
        inPlay = false;
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

    public String getVal(int i, int j) {
        return "";
    }

    public boolean CompararNums(int first, int second){
        if(getIsFinished()){
            if(first == second){
                return true;
            } else{
                return false;
            }
        }
        return false;
    }
    

    public void setIsFinished(boolean isFinished) {
        this.IsFinished = isFinished;
    }

    public boolean getIsFinished() {
        return IsFinished;
    }

    public void setFirst(int first) {
        this.first = first;
    }
    public void setSecond(int second) {
        this.second = second;
    }
    public int getFirst() {
        return first;
    }
    public int getSecond() {
        return second;
    }
    public void setInPlay(boolean inPlay) {
        this.inPlay = inPlay;
    }
    public boolean getInPlay() {
        return this.inPlay;
    }
 }
    