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

char Lampada[100] = "Lampada";
char Ventilador[100] = "Ventilador";

int main() {

	// dispositivo declarado: Lampada
	
	// dispositivo declarado: Ventilador
	
	ligar(Lampada);
	desligar(Ventilador);
	return 0;
}
