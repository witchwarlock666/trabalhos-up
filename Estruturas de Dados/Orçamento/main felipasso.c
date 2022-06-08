#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

typedef struct {
	char nome[26];
	float valor;
	//int count;
} despesa;

int countFixo = 0;
int QTDDespezas[12];
float SaldosMeses[12];

int main() {

	despesa janeiro[15], fevereiro[15], marco[15], abril[15], maio[15], junho[15], julho[15], agosto[15], setembro[15], outubro[15], novembro[15], dezembro[15];
//	float saldo1[5], saldo2[5], saldo3[5], saldo4[5], saldo5[5], saldo6[5], saldo7[5], saldo8[5], saldo9[5], saldo10[5], saldo11[5], saldo12[5];
	float ValorDFixa;
	char aaaaa[26];
	int op;
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
		printf("Digite o valor da despesa fixa:\n");
		scanf("%f", &ValorDFixa);
			janeiro[countFixo].valor = ValorDFixa;
			fevereiro[countFixo].valor = ValorDFixa;
			marco[countFixo].valor = ValorDFixa;
			abril[countFixo].valor = ValorDFixa;
			maio[countFixo].valor = ValorDFixa;
			junho[countFixo].valor = ValorDFixa;
			julho[countFixo].valor = ValorDFixa;
			agosto[countFixo].valor = ValorDFixa;
			setembro[countFixo].valor = ValorDFixa;
			outubro[countFixo].valor = ValorDFixa;
			novembro[countFixo].valor = ValorDFixa;
			dezembro[countFixo].valor = ValorDFixa;
		for( i=0; i<12; i++){
			 SaldosMeses[i] -= ValorDFixa;			
		}
		
		

//		janeiro[countFixo].count += 1;
//		fevereiro[countFixo].count += 1;
//		marco[countFixo].count += 1;
//		abril[countFixo].count += 1;
//		maio[countFixo].count += 1;
//		junho[countFixo].count += 1;
//		julho[countFixo].count += 1;
//		agosto[countFixo].count += 1;
//		setembro[countFixo].count += 1;
//		outubro[countFixo].count += 1;
//		novembro[countFixo].count += 1;
//		dezembro[countFixo].count += 1;
		for(i=0;i<12;i++){
			QTDDespezas[i]++;
		}
		
		countFixo++;
		
		printf("Deseja continuar? (sim = 1 /n = 0)\n");
		scanf("%d", &op);
		
		if (op != 1) {
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
				addDespesa(&janeiro, 0);
				break;
			case 2:
				addDespesa(&fevereiro, 1);
				break;
			case 3:
				addDespesa(&marco, 2);
				break;
			case 4:
				addDespesa(&abril, 3);
				break;
			case 5:
				addDespesa(&maio, 4);
				break;
			case 6:
				addDespesa(&junho, 5);
				break;
			case 7:
				addDespesa(&julho, 6);
				break;
			case 8:
				addDespesa(&agosto, 7);
				break;
			case 9:
				addDespesa(&setembro, 8);
				break;
			case 10:
				addDespesa(&outubro, 9);
				break;
			case 11:
				addDespesa(&novembro, 10);
				break;
			case 12:
				addDespesa(&dezembro, 11);
				break;
			}
			break;
		case 2:
			switch (mes) {
			case 1:
				addSaldo(0);
				break;
			case 2:
				addSaldo(1);
				break;
			case 3:
				addSaldo(2);
				break;
			case 4:
				addSaldo(3);
				break;
			case 5:
				addSaldo(4);
				break;
			case 6:
				addSaldo(5);
				break;
			case 7:
				addSaldo(6);
				break;
			case 8:
				addSaldo(7);
				break;
			case 9:
				addSaldo(8);
				break;
			case 10:
				addSaldo(9);
				break;
			case 11:
				addSaldo(10);
				break;
			case 12:
				addSaldo(11);
				break;
			}
			break;
		case 3:
			switch (mes) {
			case 1:
				visualizarMes(janeiro, "janeiro", 0);
				break;
			case 2:
				visualizarMes(fevereiro,"fevereiro", 1);
				break;
			case 3:
				visualizarMes(marco,"marco", 2);
				break;
			case 4:
				visualizarMes(abril,"abril", 3);
				break;
			case 5:
				visualizarMes(maio,"maio", 4);
				break;
			case 6:
				visualizarMes(junho, "junho", 5);
				break;
			case 7:
				visualizarMes(julho,"julho" , 6);
				break;
			case 8:
				visualizarMes(agosto, "agosto", 7);
				break;
			case 9:
				visualizarMes(setembro, "setembro" , 8);
				break;
			case 10:
				visualizarMes(outubro, "outubro", 9);
				break;
			case 11:
				visualizarMes(novembro,"novembro" , 10);
				break;
			case 12:
				visualizarMes(dezembro, "dezembro" , 11);
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

int addDespesa(despesa *mes, int Indmes) {
	char aaaaa[26];
	float val;
	int cont = 1;
	int i;
	QTDDespezas[Indmes]++;
//	while (cont)
//	{
//		for(i=0;i<12;i++){
//			if ( == 1) {
//			QTDDespezas[i]++;
//				}
//				else {
//				cont = 0;
//			}
//		}
	
//	}
	printf("Digite o nome da despesa:\n");
	gets(aaaaa);
	for (i = 0; i < 26; i++) {
		mes[QTDDespezas[Indmes]].nome[i] = aaaaa[i];
	}
	printf("Digite o valor da despesa:\n");
	scanf("%f", &val);
	mes[QTDDespezas[Indmes]].valor = val;
	SaldosMeses[Indmes] -= val;
}

int addSaldo(int IndMes) {
	float saldousu;
	printf("Digite o saldo desejado para o mês: ");
	scanf("%f", &saldousu);
	SaldosMeses[IndMes] += saldousu;

}

void visualizarMes(despesa *mes, char m[10], int  Indmes) {
	int i;
	printf("Despesas de %10s \n", m);
	for(i=0; i<QTDDespezas[Indmes]; i++ ){
		printf(" \nNome da despesa:  %26s\n", mes[i].nome);
		printf(" \nValor da despesa:  %f\n", mes[i].valor);
		printf("\n-------------------------\n", mes[i].nome);
	}
//	int i, j;
//	if(mes[index].count == 1){
//		printf("Não há despesas a mostrar nesse mês!");
//	}
//	else{
//		printf("\n**********Despezas de %10s*********\n", m);
//		for(i=0;i < mes[index].count; i++){
//			printf("Valor foda: ");
//		}
//	}
//
	}
					



