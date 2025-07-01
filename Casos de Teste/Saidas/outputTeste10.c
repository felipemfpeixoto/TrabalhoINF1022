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

char Camera[100] = "Camera";
char Sensor[100] = "Sensor";
char Sirene[100] = "Sirene";

int main() {

	// dispositivo declarado: Sensor
	
	// dispositivo declarado: Camera
	
	// dispositivo declarado: Sirene
	
	alerta(Sensor, "Invasao detectada!");
	alerta(Camera, "Invasao detectada!");
	alerta(Sirene, "Invasao detectada!");
	return 0;
}
