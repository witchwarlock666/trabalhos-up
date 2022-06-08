#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

typedef struct {
	char nome[26];
	float valor;
	int count;
} despesa;

int countFixo = 0;

int main() {

	despesa janeiro[15], fevereiro[15], marco[15], abril[15], maio[15], junho[15], julho[15], agosto[15], setembro[15], outubro[15], novembro[15], dezembro[15];
	float saldo1[5], saldo2[5], saldo3[5], saldo4[5], saldo5[5], saldo6[5], saldo7[5], saldo8[5], saldo9[5], saldo10[5], saldo11[5], saldo12[5];

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

		janeiro[countFixo].count += 1;
		fevereiro[countFixo].count += 1;
		marco[countFixo].count += 1;
		abril[countFixo].count += 1;
		maio[countFixo].count += 1;
		junho[countFixo].count += 1;
		julho[countFixo].count += 1;
		agosto[countFixo].count += 1;
		setembro[countFixo].count += 1;
		outubro[countFixo].count += 1;
		novembro[countFixo].count += 1;
		dezembro[countFixo].count += 1;
		
		countFixo++;
		
		printf("Deseja continuar? (s/n)\n");
		gets(aaaaa);
		
		if (aaaaa[0] != 's'&& aaaaa[0] != 'S') {
			cont = 0;
		}
	}

	cont = 1;

	while (cont) {
		int op = menu1();
		int mes = menu2();
		
		switch (op) {
		case 1:
			switch (mes) {
			case 1:
				addDespesa(&janeiro);
				break;
			case 2:
				addDespesa(&fevereiro);
				break;
			case 3:
				addDespesa(&marco);
				break;
			case 4:
				addDespesa(&abril);
				break;
			case 5:
				addDespesa(&maio);
				break;
			case 6:
				addDespesa(&junho);
				break;
			case 7:
				addDespesa(&julho);
				break;
			case 8:
				addDespesa(&agosto);
				break;
			case 9:
				addDespesa(&setembro);
				break;
			case 10:
				addDespesa(&outubro);
				break;
			case 11:
				addDespesa(&novembro);
				break;
			case 12:
				addDespesa(&dezembro);
				break;
			}
			break;
		case 2:
			switch (mes) {
			case 1:
				addSaldo(&saldo1);
				break;
			case 2:
				addSaldo(&saldo2);
				break;
			case 3:
				addSaldo(&saldo3);
				break;
			case 4:
				addSaldo(&saldo4);
				break;
			case 5:
				addSaldo(&saldo5);
				break;
			case 6:
				addSaldo(&saldo6);
				break;
			case 7:
				addSaldo(&saldo7);
				break;
			case 8:
				addSaldo(&saldo8);
				break;
			case 9:
				addSaldo(&saldo9);
				break;
			case 10:
				addSaldo(&saldo10);
				break;
			case 11:
				addSaldo(&saldo11);
				break;
			case 12:
				addSaldo(&saldo12);
				break;
			}
			break;
		case 3:
			switch (mes) {
			case 1:
				visualizarMes(janeiro, saldo1);
				break;
			case 2:
				visualizarMes(fevereiro, saldo2);
				break;
			case 3:
				visualizarMes(marco, saldo3);
				break;
			case 4:
				visualizarMes(abril, saldo4);
				break;
			case 5:
				visualizarMes(maio, saldo5);
				break;
			case 6:
				visualizarMes(junho, saldo6);
				break;
			case 7:
				visualizarMes(julho, saldo7);
				break;
			case 8:
				visualizarMes(agosto, saldo8);
				break;
			case 9:
				visualizarMes(setembro, saldo9);
				break;
			case 10:
				visualizarMes(outubro, saldo10);
				break;
			case 11:
				visualizarMes(novembro, saldo11);
				break;
			case 12:
				visualizarMes(dezembro, saldo12);
				break;
			}
			break;

		}
	}
	
}

int menu1() {
	int e;
	printf("Deseja adicionar uma despesa, adicionar saldo ou visualizar um mes? (1-3)\n");
	scanf("%d", &e);
	return e;
}

int menu2() {
	int e;
	printf("Escolha um mes: (1-12)\n");
	scanf("%d", &e);
	return e;
}

int addDespesa(despesa *mes) {
	char aaaaa[26];
	float val;
	int index = 0;
	int cont = 1;
	while (cont)
	{
		if (mes[index].count == 1) {
			index++;
		}
		else {
			cont = 0;
		}
	}
	printf("Digite o nome da despesa:\n");
	gets(aaaaa);
	for (int i = 0; i < 26; i++) {
		mes[index].nome[i] = aaaaa[i];
	}
	printf("Digite o valor da despesa:\n");
	scanf("%f", &val);
	mes[index].valor = val;
}

int addSaldo(float *saldo) {

}

int visualizarMes(despesa *mes, float *saldo) {

}
