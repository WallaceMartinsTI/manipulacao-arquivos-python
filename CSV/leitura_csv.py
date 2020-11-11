# Abrir o arquivo
arquivo = open('pessoas.csv')
# Guarda os dados do arquivo em uma variável(dados)
dados = arquivo.read()
# Fecha o arquivo
arquivo.close()

nomes = []
idades = []

# Adiciona os nomes e idades em suas respectivas listas
for registro in dados.splitlines():
    print(registro)
    nomes.append(registro.split(',')[0])
    idades.append(registro.split(',')[1])

# Printa os nomes e idades em suas posições
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

# Printa a lista dos nomes
print(nomes)
# Printa a lista das idades
print(idades)
