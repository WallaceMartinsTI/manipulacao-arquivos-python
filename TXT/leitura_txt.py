arquivo = open('pessoas.txt', 'r')
lista = arquivo.readlines()
for i in lista:
    print(f'{i}', end="")
arquivo.close()

# Criar um arquivo vazio Ou Apagar o conteúdo de um arquivo
# Certifique-se de que o arquivo não exista, se não ele irá apagar seu conteúdo
"""
arquivo = open('novo-arquivo.txt', 'w')
arquivo.close()
"""

# Escrever em um arquivo
# Se o arquivo já existir ele irá sobrescrever todo o conteúdo.
"""
arquivo = open('novo-arquivo.txt', 'w')
arquivo.write('nova linha')
arquivo.close()
Inserir conteúdo ao já existente (adicionar)

arquivo = open('nome.txt', 'r') # Abra o arquivo (leitura)
conteudo = arquivo.readlines()
conteudo.append('Nova linha')   # insira seu conteúdo

arquivo = open('nome.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()
"""
