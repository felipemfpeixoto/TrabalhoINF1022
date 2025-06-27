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

char Celular[100] = "Celular";
char Lampada[100] = "Lampada";
char Termometro[100] = "Termometro";

int main() {
    int sinal = 0;
    int temperatura = 0;

    // dispositivo declarado: Lampada
    // dispositivo Termometro com observação temperatura
    // dispositivo Celular com observação sinal
    temperatura = 42;
    ligar(Lampada);
    desligar(Lampada);
    return 0;
}
