# Cores no Terminal
# Utilizando o Padrão 'ANSI' Escape Sequence
# Código ANSI começa com \033[
# Termina com 'm'
# Entre o início e o término serão os códigos de 'style', 'text' e 'back'
# O modelo de sintax seria = \033['style'; 'text'; 'back'm
# Exemplo = \033[0:33:44m
#
# Style                 Text                Background
# 0 - Nome              20 - Branco         40 - Preto
# 1 - Bold              31 - Vermelho       41 - Vermelho
# 4 - Underline         32 - Verde          42 - Verde
# 7 - Negative          33 - Amarelo        43 - Amarelo
#                       34 - Azul           44 - Azul
#                       35 - Roxo           45 - Roxo
#                       36 - Cian           46 - Cian
#                       37 - Cinza          47 - Cinza
print('\033[mCurso em Vídeo\033[m\n')
print('\033[0;21;41mCurso em Vídeo\033[m\n')  # Neste exemplo as letras ficam em branco e toda a linha em vermelho
print('\033[4;33;44mCurso em Vídeo\033[m\n')  # Neste exemplo as letras ficam em amarelo e o fundo em azul
print('\033[1;35;43mCurso em Video\033[m\n')  # Neste exemplo as letras ficam em roxo e o fundo em amarelo
print('\033[0;30;42mCurso em Video\033[m\n')  # Neste exemplo as letras ficam em branco e o fundo em verde
print('\033[21;40mCurso em Video\033[m\n')    # Neste exemplo as letras ficam em cinza e o fundo em preto
print('\033[7;20;40mCurso em Video\033[m\n')  # Neste exemplo as letras ficam em preto e o fundo em branco
print('\033[1;33;40mCurso em Vídeo\033[m\n')
