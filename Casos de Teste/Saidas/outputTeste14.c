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
char SensorMovimento[100] = "SensorMovimento";

int main() {
    unsigned int movimento = 0;
    unsigned int temperatura = 0;

	// dispositivo Sensor com observação temperatura
	
	// dispositivo SensorMovimento com observação movimento
	
	// dispositivo declarado: Aquecedor
	
	temperatura = 15;
	movimento = 1;
	if ((temperatura < 20) && (movimento == 1)) {
		ligar(Aquecedor);
	}
	return 0;
}
