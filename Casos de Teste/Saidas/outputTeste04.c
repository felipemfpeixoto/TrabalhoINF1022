#include <stdio.h>

void ligar(char* namedevice) {
	printf("%s ligado!\n", namedevice);
}

void desligar(char* namedevice) {
	printf("%s desligado!\n", namedevice);
}

void alerta(char* namedevice, char* msg) {
	printf("%s recebeu o alerta:\n", namedevice);
	printf("%s\n", msg);
}

void alertaVariavel(char* namedevice, char* msg, unsigned int var) {
	printf("%s recebeu o alerta:\n", namedevice);
	printf("%s %d\n", msg, var);
}

char Aquecedor[100] = "Aquecedor";

int main() {
    unsigned int estaLigado = 0;
    unsigned int temperatura = 0;

	// dispositivo Aquecedor com observação temperatura
	
	temperatura = 18;
	estaLigado = 0;
	if ((temperatura < 20)) {
		ligar(Aquecedor);
	}
	return 0;
}
