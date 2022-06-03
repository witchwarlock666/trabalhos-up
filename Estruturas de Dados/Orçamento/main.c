#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

typedef struct {
	char nome[26];
	float valor;
} despesa;

int countFixo = 0;

int main() {

	despesa janeiro[15], fevereiro[15], marco[15], abril[15], maio[15], junho[15], julho[15], agosto[15], setembro[15], outubro[15], novembro[15], dezembro[15];

	char aaaaa[26];
	int i;
	int cont = 1;
	
	while (cont) {
		printf("Digite o nome da despesa fixa:\n");
		gets(aaaaa);

		for (i = 0; i < 26; i++) {
			janeiro[countFixo].nome[i] = aaaaa[i];
			fevereiro[countFixo].nome[i] = aaaaa[i];
			marco[countFixo].nome[i] = aaaaa[i];
			abril[countFixo].nome[i] = aaaaa[i];
			maio[countFixo].nome[i] = aaaaa[i];
			junho[countFixo].nome[i] = aaaaa[i];
			julho[countFixo].nome[i] = aaaaa[i];
			agosto[countFixo].nome[i] = aaaaa[i];
			setembro[countFixo].nome[i] = aaaaa[i];
			outubro[countFixo].nome[i] = aaaaa[i];
			novembro[countFixo].nome[i] = aaaaa[i];
			dezembro[countFixo].nome[i] = aaaaa[i];
		}
		
		countFixo++;
		
		printf("Deseja continuar? (s/n)\n");
		gets(aaaaa);
		
		if (aaaaa[0] != 's'&& aaaaa[0] != 'S') {
			cont = 0;
		}
	}

	cont = 1;

	while (cont) {

	}
	
}
