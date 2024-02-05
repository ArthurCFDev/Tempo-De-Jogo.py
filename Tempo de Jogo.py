def calcular_duracao_jogo(hora_inicial, minuto_inicial, hora_final, minuto_final):
    inicio_em_minutos = hora_inicial * 60 + minuto_inicial
    fim_em_minutos = hora_final * 60 + minuto_final

    if inicio_em_minutos <= fim_em_minutos:
        duracao_em_minutos = fim_em_minutos - inicio_em_minutos
    else:
        duracao_em_minutos = (24 * 60 - inicio_em_minutos) + fim_em_minutos

    return duracao_em_minutos

hora_inicial = int(input() or 0)
minuto_inicial = int(input() or 0)
hora_final = int(input() or 0)
minuto_final = int(input() or 0)

duracao_total = calcular_duracao_jogo(hora_inicial, minuto_inicial, hora_final, minuto_final)

horas = duracao_total // 60
minutos = duracao_total % 60

if horas == 0 and minutos == 0:
    horas = 24

print(f"{horas}h{minutos}m")