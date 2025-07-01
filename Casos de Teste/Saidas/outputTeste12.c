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

char Sensor[100] = "Sensor";
char Sirene[100] = "Sirene";

int main() {
    unsigned int movimento = 0;

	// dispositivo Sensor com observação movimento
	
	// dispositivo declarado: Sirene
	
	movimento = 0;
	if ((movimento != 1)) {
		ligar(Sirene);
	}
	return 0;
}
