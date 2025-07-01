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

char Lampada[100] = "Lampada";
char Termometro[100] = "Termometro";
char Ventilador[100] = "Ventilador";

int main() {
    int potencia = 0;
    int temperatura = 0;

	// dispositivo Lampada com observação potencia
	
	// dispositivo Ventilador com observação temperatura
	
	// dispositivo declarado: Termometro
	
	temperatura = 35;
	potencia = 80;
	if (temperatura > 30) {
		ligar(Ventilador);
	}
	if (potencia > 90) {
		desligar(Lampada);
	}
	alerta(Termometro, "Ambiente muito quente");
	return 0;
}
