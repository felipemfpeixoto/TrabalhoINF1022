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

char Aspersor[100] = "Aspersor";
char Sensor[100] = "Sensor";

int main() {
    unsigned int umidade = 0;

	// dispositivo Sensor com observação umidade
	
	// dispositivo declarado: Aspersor
	
	umidade = 55;
	if ((umidade <= 40)) {
		desligar(Aspersor);
	}
	return 0;
}
