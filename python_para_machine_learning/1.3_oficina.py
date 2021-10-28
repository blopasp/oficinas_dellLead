'''
Durante a aula, você aprendeu a utilizar o módulo datetime e seus tipos para trabalhar 
com informação de data e hora. Agora é a vez de praticar os seus conhecimentos. Para 
esta atividade, considere a situação e os dados a seguir.

Seus amigos sabem que você está trabalhando com Python e estão entusiasmados com as 
possibilidades de aplicações. Um deles é muito esquecido e sugeriu que você fizesse um 
programa que o alerte quando for o aniversário de alguém do seu grupo de amigos.

Você pediu aos seus amigos que anotassem as datas de seus aniversários em uma lista, 
conforme está descrito a seguir, mas cada pessoa escreveu de uma forma diferente, então, 
cabe a você interpretá-la adequadamente:

aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10', 
'12 Julho 1989', '16 de Junho de 1987', '04/07/1990'].

Para isso, o recomendado é criar uma lista de formatos correspondentes e aplicá-la à lista
de datas de aniversários. O seu objetivo é criar um programa que converta a lista de 
datas de tipo string em uma lista de objetos do tipo data e organizá-los por ordem de 
aniversário no ano. Isso significa que primeiro vem o mês e, em seguida, o dia como critério
de ordenação.

Depois, você deve verificar se o dia de hoje é aniversário de alguém. Caso seja, você deve
escrever a string “Hoje, (DIA DA SEMANA) (DIA) de (MÊS) de (ANO ATUAL), tem aniversário!”,
em que as palavras DIA DA SEMANA, DIA, MÊS e ANO ATUAL devem ser substituídas pelos seus 
respectivos valores. As informações devem estar escritas em português.

Quando você terminar, envie a resposta em um arquivo Python para a plataforma. Bom trabalho!

'''
# Funcao para converter datas
def converter_string_data(data_string):
    try:
        return datetime.strptime(data_string, '%d de %B de %Y')
    except ValueError:
        try:
            return datetime.strptime(data_string, '%d/%m/%Y')
        except ValueError:
            try:
                return datetime.strptime(data_string, '%d %B %Y')
            except ValueError:
                try:
                    return datetime.strptime(data_string, '%d/%b/%Y')
                except ValueError:
                    return datetime.strptime(data_string, '%Y-%B-%d')
    
if __name__ == '__main__':
    from datetime import datetime
    
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR')

    aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10', '12 Julho 1989', '16 de Junho de 1987', '04/07/1990']

    # Aplicando a funcao para converter datas
    aniversarios_data = list(map(converter_string_data, aniversarios))
    # Ordenando lista de datas
    aniversarios_data = sorted(aniversarios_data, key = lambda d: (d.month, d.day))
    
    # imprimindo datas ordenadas
    for data_aniver in aniversarios_data:
        print(data_aniver.strftime('%d de %B de %Y'))

    hoje = datetime.now()
    
    # Verificando de a data atual possui algum aniversario
    if hoje.strftime('%m-%d') in [data.strftime('%m-%d') for data in aniversarios_data]:
        print(f"Hoje, {hoje.strftime('%A')} {hoje.day} de {hoje.strftime('%B')} de {hoje.year}, tem aniversário!")