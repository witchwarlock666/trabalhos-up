#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {

	char nome[50];
	float val;
	int tipo;
	int mes;

} despesa;

typedef struct {

	char nome[50];
	float val;
	int mes;

} entrada;

const char* meses(int n) {

	static char* mes[] = { "Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" };

	return mes[n - 1];
}

void flush_in() {
	int ch;
	while ((ch = fgetc(stdin)) != EOF && ch != '\n') {}
}

int countMes[] = {0,0,0,0,0,0,0,0,0,0,0,0};

int main() {

	despesa contas[100] = { "null", 0, 0, 0 };
	entrada entrada[100] = { "null", 0 };
	int cont = 1;
	int index = 0;
	int indexE = 0;
	int op;

	while (cont) {
		system("cls");
		printf("====== Controle de Despesas ======\n");
		printf("\n       ------- MENU -------\n\n");
		printf(" [ 1 ] Nova Despesa \n");
		printf(" [ 2 ] Nova Entrada \n");
		printf(" [ 3 ] Listar Despesas \n");
		printf(" [ 0 ] Sair \n");

		printf("\n Informe uma Opcao: ");
		scanf("%d", &op);
		flush_in();

		switch (op) {
		case 1:
			newDespesa(&contas[index]);
			index++;
			break;
		case 2:
			newEntrada(&entrada[indexE]);
			indexE++;
			break;
		case 3:
			listDespesa(contas, index, indexE, entrada);
			break;
		case 0:
			cont = 0;
			break;
		}
	}

}

int newDespesa(despesa* despesa) {
	int op = 0;
	int i;

	system("cls");
	printf("\n------ Nova Despesa ------");
	printf("\nNome: ");
	gets((*despesa).nome);
	printf("Valor: ");
	scanf("%f", &(*despesa).val);
	flush_in();
	printf("Despesa Fixa?\n [ 1 ] Sim\n [ 2 ] Nao\n\n>>");
	scanf("%d", &op);

	while (op != 1 && op != 2) {
		printf("\nInforme uma opção valida\n\n>>");
		scanf("%d", &op);
	}

	if (op == 1) {
		(*despesa).tipo = 0;
		for (i = 0; i < 12; i++) {
			countMes[i] = 1;
		}
	}
	else {
		(*despesa).tipo = 1;
		printf("Mes: ");
		scanf("%d", &(*despesa).mes);
		while ((*despesa).mes < 1 || op > 12) {
			printf("\nInforme uma opção valida\n\n>>");
			scanf("%d", &(*despesa).mes);
		}

		countMes[(*despesa).mes -1] = 1;
	}
}

int newEntrada(entrada* entrada) {
	system("cls");
	printf("\n------ Nova Entrada ------");
	printf("\nNome: ");
	gets((*entrada).nome);
	printf("Valor: ");
	scanf("%f", &(*entrada).val);
	flush_in();
	printf("Mes: ");
	scanf("%d", &(*entrada).mes);
	flush_in();
	countMes[(*entrada).mes -1] = 1;
}

int listDespesa(despesa despesas[], int index, int indexE, entrada entradas[]) {
	int i = 0;
	int j = 0;
	for (j = 1; j <= 12; j++) {
		float totD = 0;
		float totE = 0;
		system("cls");
		if (countMes[j - 1] > 0) {
			printf("%s:\n", meses(j));
			printf("\n ---------- Listagem de Despesas ----------\n");

			printf("\n| Cod |    Nome    |    Valor     | Tipo  |\n");
			for (i = 0; i < index; i++) {
				if (despesas[i].mes == j || despesas[i].mes == 0) {
					printf("|  %.2d | %10s | R$%10.2f | %5s |\n", i, despesas[i].nome, despesas[i].val, (despesas[i].tipo == 0 ? "Fixo" : "Extra"));
					totD += despesas[i].val;
				}
			}
			//printf("\n Salário: R$%.2f\n Gasto: R$%.2f\n Saldo: R$%.2f\n\n", sal, tot, sal - tot);

			printf("\n ---------- Listagem de Entradas ----------\n");

			printf("\n|    Nome    |    Valor     |\n");
			for (i = 0; i < indexE; i++) {
				if (entradas[i].mes == j || entradas[i].mes == 0) {
					printf("| %10s | R$%10.2f |\n", entradas[i].nome, entradas[i].val);
					totE += entradas[i].val;
				}
			}

			printf("\n ----------------- Total ------------------\n");

			printf("\n|    Gasto    |    Ganho     |     Resto     |\n");
			printf("| R$%10.2f | R$%10.2f | R$%10.2f |\n", totD, totE, (totE - totD));

			system("pause");
		}
	}
	
}
