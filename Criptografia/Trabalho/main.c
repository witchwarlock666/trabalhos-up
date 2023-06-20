#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void cifra(char* msg, char* key) {
	int i;
	for (i = 0; i < strlen(msg); i++) {
		int m = i % strlen(key);
		msg[i] = ((msg[i] ^ key[m]) + key[m]);
	}
	msg[i] = '\0';
}

void decifra(char* msg, char* key) {
	int i;
	for (i = 0; i < strlen(msg); i++) {
		int m = i % strlen(key);
		msg[i] = ((msg[i] - key[m]) ^ key[m]);
	}
	msg[i] = '\0';
}



int main() {
	char a[30];
	char b[30];

	strcpy(a, "abcdefghijklmnopqrstuvwxyz");
	strcpy(b, "yb33ef44ij55mno77rstuv99y1");

	cifra(&a, &b);

	printf("%s\n\n", a);

	decifra(&a, &b);

	printf("%s\n\n", a);

	printf("Press ENTER to Continue\n");  
	getchar(); 

	return 0;
}