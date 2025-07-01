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
    unsigned int intensidade = 0;
    unsigned int movimento = 0;

	// dispositivo Sensor com observação movimento
	
	// dispositivo Alarme com observação intensidade
	
	movimento = 1;
	intensidade = 80;
	if ((movimento > 0)) {
		if ((intensidade > 70)) {
		ligar(Alarme);
	}
	}
	return 0;
}
