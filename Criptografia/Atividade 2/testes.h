#include "defines.h"
#include "cifras.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// ****************
// Funções de teste
// ****************
void testar_Cesar();
void testar_Vernam_Mauborgne();
void testar_Rail_Fence();
void testar_Vigenere();


// ******************
// Funções auxiliares
// ******************
void mostrar_chars(char *texto, int tamanho);
void avaliar(char *texto, char *esperado);
void gabarito_Vernam_Mauborgne(char * gabarito, int teste);
void remover_espaco(char *texto);