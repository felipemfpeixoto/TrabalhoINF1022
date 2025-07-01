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

char Ventilador[100] = "Ventilador";

int main() {
    unsigned int ligado = 0;
    unsigned int temperatura = 0;

	// dispositivo declarado: Ventilador
	
	temperatura = 28;
	ligado = 1;
	if ((temperatura > 25) && (ligado == 1)) {
		ligar(Ventilador);
	}
	return 0;
}
