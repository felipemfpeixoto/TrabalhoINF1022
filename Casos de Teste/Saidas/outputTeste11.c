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

char Alarme[100] = "Alarme";
char Sensor[100] = "Sensor";

int main() {
    unsigned int movimento = 0;

	// dispositivo Sensor com observação movimento
	
	// dispositivo declarado: Alarme
	
	movimento = 1;
	if ((movimento == 1)) {
		ligar(Alarme);
	}
	return 0;
}
