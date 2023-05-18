#define _CRT_SECURE_NO_WARNINGS

#include "defines.h"
#include "testes.h"
#include <stdio.h>
#include <string.h>



int main() {
   
    // ********************************
    // Avalia a corretude de cada cifra
    // ********************************
    testar_Cesar();
    testar_Vernam_Mauborgne();
    testar_Rail_Fence();
    testar_Vigenere();
     
    return 0;
}
