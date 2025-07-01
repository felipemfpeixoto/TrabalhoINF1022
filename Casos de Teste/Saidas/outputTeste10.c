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

void alertaVariavel(char* namedevice, char* msg, int var) {
	printf("%s recebeu o alerta:\n", namedevice);
	printf("%s %d\n", msg, var);
}

char Aquecedor[100] = "Aquecedor";
char Central[100] = "Central";
char Termometro[100] = "Termometro";
char Ventilador[100] = "Ventilador";

int main() {
    int msg_status = 0;
    int rotacao = 0;
    int temperatura = 0;

	desligar(Aquecedor);
	return 0;
}
