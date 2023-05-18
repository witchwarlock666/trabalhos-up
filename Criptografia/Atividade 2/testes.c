#define _CRT_SECURE_NO_WARNINGS
#include "testes.h"



// ****************************************************************
// Funções para testar as cifras
// ****************************************************************
void testar_Cesar() {
    // ***********************
    // Variáveis auxiliares
    // ***********************
    //// Texto aberto e cifrado
    char texto_aberto[MAX_TAM_TEXTO];
    char texto_cifrado[MAX_TAM_TEXTO];

    //// Solução correta
    char esperado[MAX_TAM_TEXTO];

    // ***********************************
    // Teste da cifra de César
    // ***********************************
    printf("***********************\n");
    printf("Testando cifra de César\n");
    printf("***********************\n");
    /* 1º Teste */
    printf("k = 1\n");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "bcdefghijklmnopqrstuvwayzx");
    cifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 1);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 1);
    avaliar(texto_cifrado, texto_aberto);



    /* 2º Teste */
    printf("k = 2\n");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "cdefghijklmnopqrstuvwxbzay");
    cifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 2);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 2);
    avaliar(texto_cifrado, texto_aberto);




    /* 3º Teste */
    printf("k = 3");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "defghijklmnopqrstuvwxycabz");
    cifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 3);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 3);
    avaliar(texto_cifrado, texto_aberto);




    /* 4º Teste */
    printf("k = 25");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "zabcdefghijklmnopqrstuywxv");
    cifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 25);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 25);
    avaliar(texto_cifrado, texto_aberto);




    /* 5º Teste */
     printf("k = 26");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "abcdefghijklmnopqrstuvzxyw");
    cifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 26);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 26);
    avaliar(texto_cifrado, texto_aberto);




    /* 6º Teste */
    printf("k = 27");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "bcdefghijklmnopqrstuvwayzx");
    cifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 27);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 27);
    avaliar(texto_cifrado, texto_aberto);




    /* 7º Teste */
    printf("k = 45");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "tuvwxyzabcdefghijklmnosqrp");
    cifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 45);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Cesar(texto_cifrado, strlen(texto_cifrado), 45);
    avaliar(texto_cifrado, texto_aberto);

}

void testar_Vernam_Mauborgne() {

    // ***********************
    // Variáveis auxiliares
    // ***********************
    //// Texto aberto e cifrado
    char texto_aberto[MAX_TAM_TEXTO];
    char texto_cifrado[MAX_TAM_TEXTO];

    //// Solução correta
    char esperado[MAX_TAM_TEXTO];


    //// Chave
    char k[MAX_TAM_TEXTO];

    // **********************************
    // Teste da cifra de Vernam Mauborgne
    // **********************************
    printf("**********************************\n");
    printf("Testando cifra de Vernam Mauborgne\n");
    printf("**********************************\n");


    printf("1º Teste\n");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(k,     "abcdefghijklmnopqrstuvzxyw");
    cifrar_Vernam_Mauborgne(texto_cifrado, strlen(texto_aberto), k);
    gabarito_Vernam_Mauborgne(esperado, 1); // Obtém a solução correta para o teste

    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Vernam_Mauborgne(texto_cifrado, strlen(texto_aberto), k);
    avaliar(texto_cifrado, texto_aberto);
    

    printf("2º Teste\n");
    strcpy(texto_aberto, "abcdefghijklmnopqrstuvzxyw");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(k,     "yb33ef44ij55mno77rstuv99y1");
    cifrar_Vernam_Mauborgne(texto_cifrado, strlen(texto_aberto), k);
    gabarito_Vernam_Mauborgne(esperado, 2); // Obtém a solução correta para o teste

    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

    printf("  - Decifragem: ");
    decifrar_Vernam_Mauborgne(texto_cifrado, strlen(texto_aberto), k);
    avaliar(texto_cifrado, texto_aberto);
}

void testar_Rail_Fence() {
    // ***********************
    // Variáveis auxiliares
    // ***********************
    //// Texto aberto e cifrado
    char texto_aberto[MAX_TAM_TEXTO];
    char texto_cifrado[MAX_TAM_TEXTO];

    //// Solução correta
    char esperado[MAX_TAM_TEXTO];


    // *************************
    // Teste da cifra Rail Fence
    // *************************
    printf("*************************\n");
    printf("Testando cifra Rail Fence\n");
    printf("*************************\n");

    /* 1º Teste */
    printf("k = 1\n");
    strcpy(texto_aberto, "OLA MEU NOME E X");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "OLAMEUNOMEEX");
    cifrar_Rail_Fence(texto_cifrado, strlen(texto_cifrado), 1);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

       

    /* 2º Teste */
    printf("k = 2\n");
    strcpy(texto_aberto, "OLA MEU NOME E X");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "OAENMELMUOEX");
    cifrar_Rail_Fence(texto_cifrado, strlen(texto_cifrado), 2);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);


    /* 3º Teste */
    printf("k = 3\n");
    strcpy(texto_aberto, "OLA MEU NOME E X");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(esperado, "OEMLMUOEXANE");
    cifrar_Rail_Fence(texto_cifrado, strlen(texto_cifrado), 3);
    
    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

}

void testar_Vigenere() {
    // ***********************
    // Variáveis auxiliares
    // ***********************
    //// Texto aberto e cifrado
    char texto_aberto[MAX_TAM_TEXTO];
    char texto_cifrado[MAX_TAM_TEXTO];

    //// Solução correta
    char esperado[MAX_TAM_TEXTO];

    //// Chave
    char k[MAX_TAM_TEXTO];

    // **************************
    // Teste da cifra de Vigenère
    // **************************
    printf("**************************\n");
    printf("Testando cifra de Vigenère\n");
    printf("**************************\n");

    printf("1º Teste\n");
    strcpy(texto_aberto, "OLA MEU NOME E X");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(k,     "BATATA");
    strcpy(esperado, "PLT MXU OOFE X X");
    cifrar_Vigenere(texto_cifrado, strlen(texto_cifrado), k);
    

    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);


    printf("2º Teste\n");
    strcpy(texto_aberto, "BEM VINDO A ROMA");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(k,     "ESCRIBA");
    strcpy(esperado, "FWO MQODS S TFUB");
    cifrar_Vigenere(texto_cifrado, strlen(texto_cifrado), k);
    

    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);


    printf("3º Teste\n");
    strcpy(texto_aberto, "BEM VINDO A ROMA");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(k,     "PAPIRO");
    strcpy(esperado, "QEB DZBSO P ZFAP");
    cifrar_Vigenere(texto_cifrado, strlen(texto_cifrado), k);
    

    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);


    printf("4º Teste\n");
    strcpy(texto_aberto, "NEVER");
    strcpy(texto_cifrado, texto_aberto);
    strcpy(k,     "GONNAGIVEYOUUP");
    strcpy(esperado, "TSIRR");
    cifrar_Vigenere(texto_cifrado, strlen(texto_cifrado), k);
    

    //// Avaliando o resultado
    printf("  - Cifragem: ");
    avaliar(texto_cifrado, esperado);

}

// ****************************************************************
// Funções auxiliares
// ****************************************************************
void mostrar_chars(char *texto, int tamanho) {
    for (int i=0; i<MAX_TAM_TEXTO; i++) {
        printf(" %d", texto[i]);
    }
    printf("\n");
}

void avaliar(char *texto, char *esperado) {
    //// Avaliando o resultado
    if (strcmp(texto, esperado) != 0) {
        printf("- ERRO\n");
        printf("    Resultado esperado: %s\n", esperado);
        printf("    Resultado obtido: %s\n", texto);
        printf("Em decimal:\n");
        printf("    Esperado:"); mostrar_chars(esperado, strlen(esperado));
        printf("    Obtido  :"); mostrar_chars(texto, strlen(texto));
    }
    else {
        printf(" - OK\n");
    }
}


void gabarito_Vernam_Mauborgne(char * gabarito, int teste) {
    switch(teste) {
        case 1:
            memset(gabarito, 0, sizeof(char)*MAX_TAM_TEXTO);
            break;

        case 2:
            memset(gabarito, 0, sizeof(char)*MAX_TAM_TEXTO);
            gabarito[0] = 24;
            gabarito[1] = 0;
            gabarito[2] = 80;
            gabarito[3] = 87;
            gabarito[4] = 0;
            gabarito[5] = 0;
            gabarito[6] = 83;
            gabarito[7] = 92;
            gabarito[8] = 0;
            gabarito[9] = 0;
            gabarito[10] = 94;
            gabarito[11] = 89;
            gabarito[12] = 0;
            gabarito[13] = 0;
            gabarito[14] = 0;
            gabarito[15] = 71;
            gabarito[16] = 70;
            gabarito[17] = 0;
            gabarito[18] = 0;
            gabarito[19] = 0;
            gabarito[20] = 0;
            gabarito[21] = 0;
            gabarito[22] = 67;
            gabarito[23] = 65;
            gabarito[24] = 0;
            gabarito[25] = 70;
            gabarito[26] = 0;
            gabarito[27] = 0;
            gabarito[28] = 0;
            gabarito[29] = 0;
            gabarito[30] = 0;
            gabarito[31] = 0;
            gabarito[32] = 0;
            gabarito[33] = 0;
            gabarito[34] = 0;
            gabarito[35] = 0;
            gabarito[36] = 0;
            gabarito[37] = 0;
            gabarito[38] = 0;
            gabarito[39] = 0;
            gabarito[40] = 0;
            gabarito[41] = 0;
            gabarito[42] = 0;
            gabarito[43] = 0;
            gabarito[44] = 0;
            break;

        default:
            printf("ERRO! Teste não definido!\n");
    }
}

void remover_espaco(char *texto) {
    char *s, *t = texto;
    while(*(t+1)) {
        if (*(s = t) == ' ') {
            while(*(s+1)){
                *s = *(s+1);
                s++;
            }
            *s = *(s+1);
        }
        t++;
    }
}