#ifndef __CIFRAS__
#define __CIFRAS__
#include "defines.h"
#include <inttypes.h>


// *****************************************************************
// Cabeçalhos dos cifradores
//  - Cada cifrador recebe como parâmetro:
//      * o texto aberto
//      * o tamanho do texto
//      * a chave para encriptar
// Ao fim da execução, o texto deve estar cifrado
// *****************************************************************

void cifrar_Cesar(char *texto, int tamanho, int chave);
void cifrar_Vernam_Mauborgne(char *texto, int tamanho, char *chave);
void cifrar_Rail_Fence(char *texto, int tamanho, uint32_t chave);
void cifrar_Vigenere(char *texto, int tamanho, char *chave);


// *****************************************************************
// Cabeçalhos dos decifradores
//  - Cada cifrador recebe como parâmetro:
//      * o texto aberto
//      * o tamanho do texto
//      * a chave para encriptar
// Ao fim da execução, o texto deve estar decifrado
// *****************************************************************
void decifrar_Cesar(char *texto, int tamanho, int chave);
void decifrar_Vernam_Mauborgne(char *texto, int tamanho, char *chave);

#endif