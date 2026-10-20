notas = []
for i in range(5):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

soma = 0
for nt in notas:
    soma += nt

media = soma/len(notas)

print(f'Notas: {notas}')
print(f'Soma: {soma}')
print(f'Média: {media:.1f}')
print(f'Menor nota: {min(notas)}')
print(f'Maior nota: {max(notas)}')


#Notas: [7.5, 8.0, 6.5, 9.0, 7.0]
#Soma: 38.0
#Média: 7.6
#Menor nota: 6.5
#Maior nota: 9.0