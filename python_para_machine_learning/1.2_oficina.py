import re

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

if __name__ == '__main__':

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

    for horario in count_horario:
        print(f'Horario {horario[0]}h Ocorrencias: {horario[1]}')