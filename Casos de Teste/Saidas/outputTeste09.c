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

char Camera[100] = "Camera";
char Portao[100] = "Portao";

int main() {
    int status = 0;

	// dispositivo Portao com observação status
	
	// dispositivo declarado: Camera
	
	status = 0;
	if (status <= 0) {
		ligar(Portao);
	}
	if (status > 0) {
		desligar(Portao);
	}
	alerta(Camera, "Portao foi aberto");
	return 0;
}
