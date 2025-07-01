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

char Computador[100] = "Computador";
char Termometro[100] = "Termometro";
char Ventilador[100] = "Ventilador";

int main() {
    int potencia = 0;
    int temperatura = 0;

	// dispositivo Termometro com observação temperatura
	
	// dispositivo Ventilador com observação potencia
	
	// dispositivo declarado: Computador
	
	temperatura = 40;
	potencia = 90;
	ligar(Ventilador);
	ligar(Computador);
	alerta(Termometro, "Mensagem");
	if (temperatura > 30) {
		ligar(Ventilador);
	}
	if (temperatura < 30) {
		desligar(Ventilador);
	}
	if (temperatura >= 30) {
		ligar(Ventilador);
	}
	if (temperatura <= 30) {
		desligar(Ventilador);
	}
	return 0;
}
