"""
Oficina Aula 2

Olá! Esta oficina será dividida em duas etapas. Leia cada uma com atenção e faça o 
que se pede.

ETAPA 1

Pedra, papel e tesoura, também chamado de jokempô dependendo da região do Brasil, 
é um jogo de mãos recreativo e simples para duas ou mais pessoas que não requer 
equipamentos nem habilidade. Esse jogo contém um pouco de aleatoriedade, que é um
 assunto que você estudou durante este curso.

No jogo, cada jogador deve, simultaneamente, esticar a mão formando um símbolo (que
significa pedra, papel ou tesoura) com a mão. Então, os jogadores comparam os 
símbolos para decidir quem ganha, da seguinte forma:

    Pedra (punho fechado) ganha da tesoura, pois a pedra quebra a tesoura.
    Tesoura (dedo indicador e dedo médio) ganha do papel, cortando-o.
    Papel (mão aberta) ganha da pedra, embrulhando-a.

Caso dois jogadores façam o mesmo gesto, ocorre um empate e, geralmente, é preciso 
jogar novamente para desempatar.

Bom, com base nesse contexto, nesta primeira etapa da oficina, escreva um código que
utilize a biblioteca Random para recriar esse jogo. O jogo só precisa dar as opções:
pedra, papel, tesoura e sair, para o jogador escolher. O jogador pode escolher 
qualquer uma das opções, mas o jogo só finaliza quando o jogador escolher a opção 
sair. Ao finalizar, envie seu código como resposta desta primeira etapa, depois disso,
avance para a segunda parte da oficina. O texto a seguir exemplifica o que deve 
aparecer na tela.

    Escolha uma opção (1, 2, 3 ou 4):
    1-Pedra
    2-Papel
    3-Tesoura
    4-Sair
    1
    Sua jogada -> Pedra
    Jogada da máquina -> Tesoura
    Você ganhou!

ETAPA 2

Agora atente-se à segunda etapa da oficina.

Como você já desenvolveu um jogo de pedra, papel e tesoura, no qual a máquina se 
utiliza somente do elemento da sorte para ganhar de outro jogador, melhore as sugestões
que a máquina fornece.

Diferentemente de outros jogos que se baseiam exclusivamente em sorte, saiba que pedra, 
papel e tesoura pode ser jogado com um pouco de habilidade. Principalmente se o jogo se 
estender por vários turnos com o mesmo jogador. Isso porque ele pode reconhecer e explorar
a lógica do comportamento do adversário, ou seja, perceber e antecipar as jogadas do 
adversário.

Sabendo disso, faça com que a máquina aprenda como ganhar do adversário utilizando Machine
Learning. Para isso, utilize o algoritmo ZeroR, que é um simples algoritmo de ML. Ele tem
o papel de selecionar a classe (pedra, papel ou tesoura) com a maior probabilidade de 
aparecer. Apesar de ele não ser um bom classificador, muitas vezes, é usado como uma linha
de base para saber se um determinado algoritmo tem um bom desempenho.

A dica é: de acordo com as jogadas do adversário, faça com que a máquina identifique qual
é o símbolo que ele mais utiliza e, sabendo disso, faça a máquina escolher o símbolo que
ganhará do símbolo que ele mais usa.

Utilize o código que você já tem – da etapa anterior – e crie essa nova funcionalidade. 
Lembre-se de que, como a máquina não tem um histórico de jogadas do adversário ao início
da partida, você deve iniciar as primeiras jogadas de forma aleatória para, depois, 
começar a utilizar o algoritmo de ML, certo? Você pode fazer com que, após o quinto turno,
ao invés de a máquina fazer uma jogada aleatória, ela chame um método que recebe a lista
de jogadas anteriores do jogador e retorne qual foi a jogada mais usada.

Ao finalizar, envie seu código como resposta.

Bom trabalho!
"""

def valida_opcao(opcao, max, min):
    return min <= opcao <= max

def comparacao(jogador_1, jogador_2):
    if (jogador_1 == 1) and (jogador_2 == 2):
        return False
    elif (jogador_1 == 1) and (jogador_2 == 3):
        return True
    elif (jogador_1 == 2) and (jogador_2 == 1):
        return True
    elif (jogador_1 == 2) and (jogador_2 == 3):
        return False
    elif (jogador_1 == 3) and (jogador_2 == 1):
        return False
    elif (jogador_1 == 3) and (jogador_2 == 2):
        return True

# funcao q realiza a jogada da maquina de forma aleatoria
def maquina(jogadas):
    jogada_random = random.choice(jogadas)
    return jogada_random, jogadas.index(jogada_random) 


if __name__ == '__main__':
    import random

    jogadas = ['Pedra', 'Papel', 'Tesoura']

    menu = """
        Escolha uma opção (1, 2, 3 ou 4):
        1-Pedra
        2-Papel
        3-Tesoura
        4-Sair
    """
    
    a = 0
    while True:
        print(menu)

        jogada_maquina, index_maquina = maquina(jogadas)

        try:
            jogada_usuario = int(input())
        except: 
            print('Por favor, escolha um numero dentre as opcoes')
            continue
        
        if valida_opcao(jogada_usuario, 4, 1):
            if jogada_usuario == 4:
                break
            
            print(f'Sua jogada -> {jogadas[jogada_usuario-1]}')
            print(f'Jogada da máquina -> {jogada_maquina}')        

            if jogada_usuario == (index_maquina+1):
                print('Empate')
            elif comparacao(jogada_usuario, (index_maquina+1)):
                print("Voce Ganhou!")
            else:
                print("Voce perdeu!")
        else:
            print('Por favor, digite uma opcao dentro da faixa indicada')
            continue
        
        print('\nRodada %d'%(a+1))
        a += 1
        


        