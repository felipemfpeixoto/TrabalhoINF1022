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

char Luz[100] = "Luz";
char Sensor[100] = "Sensor";

int main() {
    unsigned int timer = 0;

	// dispositivo declarado: Sensor
	
	// dispositivo declarado: Luz
	
	timer = 18;
	if ((timer <= 18)) {
		if ((timer > 19)) {
		ligar(Sensor);
	}
	}
	return 0;
}
