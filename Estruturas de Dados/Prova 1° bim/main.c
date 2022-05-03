#include <stdio.h>
#include <stdlib.h>

typedef struct{

	int codigo;
	
	char nome_produto[21];
	
	float preco;
	
	int quantidade_estoque;

} tipo_produto;



int main() {
	tipo_produto produtos[5] = {{1, "Arroz", 6.99, 100}, {2, "Feijao", 6.35, 100}, {3, "Macarrao", 7.95, 100}, {4, "Cafe", 10.15, 100}, {5, "Acucar", 4.39, 100}};

	int cont = 1;
	float total = 0;
	
	while (cont != 0) {
		int quantidade = 0;
		
		printf("Digite o codigo do produto: ");
		scanf("%d", &cont);
		
		if (cont != 0) {
			
			printf("Digite a quantidade do produto: ");
			scanf("%d", &quantidade);
		
			checaEstoque(cont, quantidade, &total, &produtos);
		}
	}
	
	printf("Total: R$ %.2f\n\n ", total);
	
	int i = 0;
	
	for (i = 0; i < 5; i++) {
		printf("%s: %d\n", produtos[i].nome_produto, produtos[i].quantidade_estoque);
	}
	
}

checaEstoque (int i, int quant, float* total, tipo_produto* produtos) {
	if (quant <= produtos[i-1].quantidade_estoque) {
		produtos[i-1].quantidade_estoque = produtos[i-1].quantidade_estoque - quant;
		*total += produtos[i-1].preco * quant;
	}
}


