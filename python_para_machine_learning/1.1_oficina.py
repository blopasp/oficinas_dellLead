"""
Oficina Aula 1.1

Depois de aprender bastante sobre programação funcional nesta aula, chegou o momento
de colocar seus conhecimentos em prática para resolver o problema proposto nesta oficina. 
Para isso, imagine o seguinte caso:

    Você foi chamado para trabalhar como novo programador Python para o aplicativo Spotify,
    analisando as avaliações de músicas pelos usuários. O seu chefe está muito entusiasmado
    com a sua chegada e já pensou em várias perguntas para você responder. Ele coletou 
    diversas avaliações dos gêneros musicais Rock e Pop.
    Em cada avaliação o usuário pode dar uma nota em quantidade de estrelas para uma música,
    de 1 a 5. Ele quer que você mapeie as avaliações numéricas em categorias: entre 0 e 1 
    estrelas é uma música ruim, entre 2 e 3 é uma música mediana e entre 4 e 5 são para as
    músicas boas. O seu papel é dizer para o seu chefe quantas músicas ruins, medianas e 
    boas existem para cada gênero: Rock e Pop.

    Além disso, ele quer saber se existe alguma música mediana de Rock e se todas as músicas
    de Pop são boas. Por fim, quer saber qual gênero musical teve uma maior quantidade de 
    músicas boas. Abaixo seguem as notas de cada gênero.

notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

Pronto, com essas informações você pode começar a desenvolver um programa em Python capaz de
responder as perguntas do seu chefe.

Boa prática!

"""
# Funcao para avaliar qualitivamente as notas recebidas
def avaliacao_musicas(x):
    if x >= 4:
        return 'boa'
    elif x >=3:
        return 'mediana'
    else:
        return 'ruim'
    
if __name__ == '__main__': 

    notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
    notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

    # notas avaliadas de acordo com as categorias boa, mediana e ruim
    notas_rock_avaliadas = list(map(avaliacao_musicas, notas_rock))
    notas_pop_avaliadas = list(map(avaliacao_musicas, notas_pop))

    # Notas avaliadas em formato booleano
    notas_rock_medianas_booleano = list(map(lambda nota: nota == 'mediana', notas_rock_avaliadas))
    notas_pop_boas_booleano = list(map(lambda nota: nota == 'boa', notas_pop_avaliadas))

    # Mostrar se ha alguma musica de rock que eh mediana
    print(any(notas_rock_medianas_booleano))

    # Mostrar se todas as musicas de pop sao boas
    print(all(notas_pop_boas_booleano))
