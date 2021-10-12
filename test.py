# Itertools

import itertools

contador = itertools.count()

print(next(contador))

print(list(itertools.combinations('ABC', 3)))

print(list(itertools.permutations(['C', 'B', 'A'], r = 3)))

print(list(itertools.product([1, 2], [4, 5])))

print(list(itertools.product(['Python'], ['Academy', 'Rocks']))) 

# Expressoes Regulares
# regex (regular expression)

print('\t tabulacao')
print(r'\t tabulacao')

import re

palavra = r'otorrinolaringologista 816'

print(re.search(r'rino', palavra))

print(re.search(r'ri', palavra))

print(re.search('\d', palavra).group())
print(re.search('test', palavra))

dados = r"""Laura Maria da Silva\n(46) 93201-6392\n(89) 42010-7411\n(61) 47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell
                                                    Technologies"""
# fazendo busca atraves de expressoes regulares
re.search(r'[0-9][0-9]', dados)

# \W significa caractere nao verbal
re.findall(r'\W[0-9][0-9]\W', dados)

# utilizando quantificadores em expressoes regulares
re.findall(r'\W[0-9]{2}\W', dados)

# para procurar o ddd
re.findall(r'\W\d{2}\W', dados)

# para encontrar o numero sem o ddd
re.findall(r'\d{5}\W\d{4}', dados)

# para encontrar o numero com o ddd
re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}', dados)

# para encontrar com e sem o ddd atraves do ou (|)
re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}|\d{5}\W\d{4}', dados)

# usando expressoes regulares para encontrar padroes de email
palavra = r'contato@dellead.com, franciscojose@yahoo.com.br, ana.julia@universidade.edu, francisca-321-aline@meu-trabalho.net, Le@d Dell Technologies'

# Antes do @
re.findall(r'[a-zA-Z0-9_.-]+@', palavra)

# apos @
re.findall(r'@[a-zA-Z0-9_.-]+\.[a-zA-Z0-9_.-]+', palavra)

# emails completos
re.findall(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z0-9_.-]+', palavra)


# criacao de loggs
import logging

# formato de saida de cada linha do logger
FORMATACAO_MSG = "%(asctime)s | %(levelname)s -> %(message)s"
# criacao e configuracao do objeto logger
logging.basicConfig(filename='logs.log', 
                    level=logging.DEBUG, 
                    format=FORMATACAO_MSG,
                    filemode='w')
logger = logging.getLogger()

# Testando o logger
logger.debug('depuracao')
logger.info('informacao')
logger.warning('aviso')
logger.error('erro')
logger.critical('critico')

logger.info('O programa foi iniciado')

for i in range(3):
    try:
        logger.debug('Iteração número {0}'.format(i))
        print('Vamos dividir dois números!')

        num_1 = int(input('Digite o primeiro número:'))
        logger.debug('O usuário digitou o primeiro número: {0}'.format(num_1))

        num_2 = int(input('Digite o segundo número:'))
        logger.debug('O usuário digitou o segundo número: {0}'.format(num_2))

        resultado = num_1/num_2
        print('O resultado é',resultado)
        logger.debug('O resultado da operação: {0}'.format(resultado))
    
    except ZeroDivisionError:
        print('Essa operação é impossível')
        logger.warning('O usuário tentou fazer uma divisão por 0')

    except Exception as erro:
        print('Erro, tente novamente!')
        logger.error('Erro não esperado -> '+str(erro))

    finally:
        print('----------------------')

logger.info('O programa foi finalizado')

msg_log = """
2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida

"""

import re

erro_program = re.findall(r'\s\d{2}\W\d{2}\W\d{2}\W\d{3}\s\W\s[ERROR]+', msg_log)

print(erro_program)

horario_ocorrencia = [re.findall(r'\d{2}', x)[0] for x in erro_program]

count_horario = []

for horario in horario_ocorrencia:
    if horario not in [x[0] for x in count_horario]:
        c = 0
        for i in range(len(horario_ocorrencia)):
            if horario == horario_ocorrencia[i]:
                c += 1
        count_horario.append([horario, c])
    else: continue



print(count_horario)

