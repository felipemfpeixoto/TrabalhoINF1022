#!/bin/bash

# Loop de 1 a 10
for i in $(seq -w 1 15); do
    arquivo="Casos de Teste/Saidas/outputTeste${i}.c"
    if [[ -f "$arquivo" ]]; then
        echo "Compilando $arquivo..."
        gcc "$arquivo" -o "Casos De Teste/SaidasCompiladas/outputTeste0${i}"
        echo "Arquivo $arquivo compilado com sucesso."
        ./"Casos De Teste/SaidasCompiladas/outputTeste0${i}"

        echo "Execucao terminou"
    else
        echo "Arquivo $arquivo não encontrado."
    fi
done
