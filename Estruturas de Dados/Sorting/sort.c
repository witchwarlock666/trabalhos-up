#include <stdio.h>

int vetor[10] = {
	7, 4, 1, 5, 6, 9, 3, 8, 2, 0
};

int main() {
	insertion();
	reset();
	printf("\n");
	selection();
	reset();
	printf("\n");
	bubble();
}

int reset() {
	vetor[0] = 7;
	vetor[1] = 4;
	vetor[2] = 1;
	vetor[3] = 5;
	vetor[4] = 6;
	vetor[5] = 9;
	vetor[6] = 3;
	vetor[7] = 8;
	vetor[8] = 2;
	vetor[9] = 0;
}

int insertion() {
	int i, j, elemento;

	for (j = 1; j < 10; j++) {
		elemento = vetor[j];
		i = j - 1;

		while (i >= 0 && vetor[i] > elemento) {
			vetor[i + 1] = vetor[i];
			i = i - 1;
			vetor[i + 1] = elemento;
		}
	}

	printf("[ ");
	for (i = 0; i < 10; i++) {
		printf("%d ", vetor[i]);
	}
	printf("]");
}

int selection() {
	int i, j, menor, aux;

	for (i = 0; i < 10; i++) {
		menor = i;
		for (j = i + 1; j < 10; j++) {
			if (vetor[j] < vetor[menor]) menor = j;
		}
		aux = vetor[menor];
		vetor[menor] = vetor[i];
		vetor[i] = aux;
	}
	printf("[ ");
	for (i = 0; i < 10; i++) {
		printf("%d ", vetor[i]);
	}
	printf("]");
}

int bubble() {
	int i, j, aux;

	for (i = 10; i > 0; i--) {
		for (j = 1; j < i; j++) {
			if (vetor[j - 1] < vetor[j]) {
				aux = vetor[j];
				vetor[j] = vetor[j - 1];
				vetor[j - 1] = aux;
			}
		}
	}
	printf("[ ");
	for (i = 0; i < 10; i++) {
		printf("%d ", vetor[i]);
	}
	printf("]");
}
