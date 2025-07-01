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

char ArCondicionado[100] = "ArCondicionado";

int main() {
    unsigned int temperatura = 0;

	// dispositivo declarado: ArCondicionado
	
	temperatura = 30;
	if ((temperatura > 25)) {
		ligar(ArCondicionado);
	}
	return 0;
}
