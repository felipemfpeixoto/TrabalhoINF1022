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

char Cortina[100] = "Cortina";

int main() {
    unsigned int luminosidade = 0;

	// dispositivo Cortina com observação luminosidade
	
	luminosidade = 600;
	if ((luminosidade > 500)) {
		desligar(Cortina);
	}
	if ((luminosidade <= 500)) {
		ligar(Cortina);
	}
	return 0;
}
