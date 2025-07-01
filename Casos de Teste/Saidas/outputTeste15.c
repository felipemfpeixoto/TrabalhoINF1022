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

char Aquecedor[100] = "Aquecedor";
char Sensor[100] = "Sensor";
char Ventilador[100] = "Ventilador";

int main() {
    unsigned int hora = 0;
    unsigned int temperatura = 0;

	// dispositivo declarado: Aquecedor
	
	// dispositivo declarado: Ventilador
	
	// dispositivo Sensor com observação temperatura
	
	temperatura = 25;
	hora = 13;
	if ((temperatura == 20) && (hora <= 13) && (temperatura != 48)) {
		ligar(Sensor);
	} else {
		desligar(Sensor);
	}
	alerta(Aquecedor, "Atenção");
	alerta(Ventilador, "Atenção");
	return 0;
}
