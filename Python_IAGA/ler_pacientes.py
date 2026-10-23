import Calculadora_IMC
import Geral

arquivo = open("pacientes.txt", "r")
linhas = arquivo.readlines()
for linha in linhas:
    partes = linha.split("; ")
    
    paciente = partes[0]
    pc = float(partes[1])
    alt = float(partes[2])
    
    print(Calculadora_IMC.toString(paciente, pc, alt))

arquivo.close()
