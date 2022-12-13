# ***** FATIAMENTO *****
frase = 'Curso em Vídeo Python'
print()
print(frase)                                # Imprime a frase
print(frase[9])                             # Imprime somente a letra na posição 9, pois a string se inicia em 0
print(frase[9:13])                          # Imprime entre a posição 9 e vai até a letra 13, exeto a letra na posição 13
print(frase[:5])                            # Imprime do início até a posição 5 exeto a posição 5
print(frase[9:])                            # Imprime da posição 9 até o final
print(frase[::2])                           # Imprime a frase pulando de 2 em 2 caractere

# ***** ANÁLISE *****
print(len(frase))                           # Conta quantas posições tem a string
print(frase.count('o'))                     # Conta quantas vezes aparece a letra 'o'
print(frase.count('o', 0, 13))              # Conta quantas letras "o" tem até a posisão 13
print(frase.find('deo'))                    # Indica onde se inicia a procura
print(frase.find('android'))                # Significa que ele não encontrou nada, retorna -1
print('Curso' in frase)                     # Verifica se existe a palavra "Curso" dentro da string e retorna verdadeiro "True"

# ***** TRANSFORMAÇÃO *****
print(frase.replace('Python', 'Android'))   # Subistitui a palavra "Python" pela palavra "Android"
print(frase.upper())                        # Exibe na tela a string em maiúscula
print(frase.lower())                        # Exibe na tela a string em minúscula
print(frase.capitalize())                   # Altera todas as letras da string para minúscula, exeto a primeira letra na posição 0
print(frase.title())                        # Analisa as palavras e altera as primeiras palavras em maiúsculas
frase = '   Aprenda Python  '
print(frase)
print(frase.strip())                        # Remove o excesso de espaços em branco da string
print(frase.rstrip())                       # Remove somente os espaços em branco da direita da string
print(frase.lstrip())                       # Remove somente os espaços em branco da esquerda da string

# ***** DIVISÃO *****
frase = 'Curso em Vídeo Python'
print(frase)
print(frase.split())                        # Gera uma nova lista e gera uma nova indexação

# ***** JUNÇÃO *****
frase = ['Curso', 'em', 'Video', 'Python']
print(' '.join(frase))                      # Junta todos as strings de uma lista e acrescenta um espaço ou qualquer outro caractere
