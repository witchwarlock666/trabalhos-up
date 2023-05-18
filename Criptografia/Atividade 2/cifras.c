#include "cifras.h"

void re(char* texto);

void cifrar_Cesar(char* texto, int tamanho, int chave) {
	for (int i = 0; i < tamanho; i++) {
		texto[i] += chave;
		while (texto[i] > 122 || texto[i] < 97) {
			texto[i] -= 26;
		}
	}
}

void decifrar_Cesar(char* texto, int tamanho, int chave) {
	for (int i = 0; i < tamanho; i++) {
		texto[i] -= chave;
		while (texto[i] > 122 || texto[i] < 97) {
			texto[i] += 26;
		}
	}
}

void cifrar_Vernam_Mauborgne(char* texto, int tamanho, char* chave) {
	for (int i = 0; i < tamanho; i++) {
		texto[i] = texto[i] ^ chave[i];
	}
}

void decifrar_Vernam_Mauborgne(char* texto, int tamanho, char* chave) {
	for (int i = 0; i < tamanho; i++) {
		texto[i] = texto[i] ^ chave[i];
	}
}

void cifrar_Rail_Fence(char* texto, int tamanho, uint32_t chave)
{
	re(texto);

	if (chave == 1) return;
	
	int a = (chave - 1) * 2;

	int size = strlen(texto);

	char cifra[size];

	int j = 0;
	for (int i = 0; i < chave; i++)
	{
		int step = a - 2 * i;
		int k = i;
		while (k < size)
		{
			cifra[j++] = texto[k];
			if (step != a && step != 0 && k + step < size)
				cifra[j++] = texto[k + step];
			k += a;
		}
	}
	cifra[j] = '\0';
	
	strcpy(texto, cifra);
}

void cifrar_Vigenere(char* texto, int tamanho, char* chave) {
	int keySize = strlen(chave);

	int j = 0;
	for (int i = 0; i < tamanho; i++) {
		if (texto[i] != ' ') {
			texto[i] = ((texto[i] + chave[j++ % keySize]) % 26) + 65;
		}
	}
}

void re(char* texto) {
	char* s, * t = texto;
	while (*(t + 1)) {
		if (*(s = t) == ' ') {
			while (*(s + 1)) {
				*s = *(s + 1);
				s++;
			}
			*s = *(s + 1);
		}
		t++;
	}
}